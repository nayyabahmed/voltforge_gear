#!/usr/bin/env python3
"""
build_book.py — assemble the VoltForge Gear handbook into a published artifact
(PDF / EPUB / HTML) from the Markdown source.

Pipeline
--------
1. Read SUMMARY.md — the single source of truth for chapter ORDER and which
   chapters are published (a chapter counts as published when its table row
   links to a real .md file that exists on disk).
2. For each chapter:
     - strip the YAML front matter,
     - inject its full-page cover image (assets/chapter_covers/Chapter NN Cover.png)
       as a chapter-opener page, if one exists,
     - pre-render every ```mermaid block to an SVG with mermaid-cli (mmdc),
       because PDF/EPUB engines cannot run Mermaid.
3. Concatenate everything (with Part dividers) into build/combined.md.
4. Hand that to Pandoc to produce the requested output(s).

Covers and Mermaid images live in assets/ and build/ — never in the prose —
so the Markdown stays clean and keeps rendering on GitHub.

This script SHELLS OUT to `mmdc` and `pandoc`; see BUILD.md for how to install
them. Use `--list` first — it parses SUMMARY.md and reports what it found
WITHOUT needing any external tool.

Usage
-----
    python scripts/build_book.py --list                 # dry run, no deps
    python scripts/build_book.py --pdf                   # -> dist/VoltForgeGear.pdf
    python scripts/build_book.py --epub --html           # multiple targets
    python scripts/build_book.py --pdf --no-mermaid      # skip diagram pre-render
    python scripts/build_book.py --pdf --include-glossary
    python scripts/build_book.py --pdf --chapters 00,01  # partial build
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------- paths
ROOT       = Path(__file__).resolve().parent.parent
SUMMARY    = ROOT / "SUMMARY.md"
COVERS_DIR = ROOT / "assets" / "chapter_covers"
TITLE_PAGE = ROOT / "assets" / "tile_page" / "Title_page.png"
BUILD      = ROOT / "build"
MERMAID    = BUILD / "mermaid"
DIST       = ROOT / "dist"
CSS        = ROOT / "scripts" / "print.css"
TITLE      = "VoltForge Gear — The Young Engineer's Handbook"

# ---------------------------------------------------------------- regexes
LINK_RE     = re.compile(r"\[([^\]]+)\]\(([^)]+?\.md)\)")
FRONTMATTER = re.compile(r"\A﻿?---\r?\n.*?\r?\n---\r?\n", re.S)
MERMAID_RE  = re.compile(r"```mermaid[^\n]*\n(.*?)\n```", re.S)
CHAPNUM_RE  = re.compile(r"(\d{2})[-_]")
H1_RE       = re.compile(r"^# (.+?)\s*$", re.M)


def chapter_number(path: Path) -> str | None:
    m = CHAPNUM_RE.match(path.name)
    return m.group(1) if m else None


def filter_chapters(items: list[dict], wanted: set[str]) -> list[dict]:
    """Keep only chapters whose NN- prefix is in `wanted`, dropping empty parts."""
    kept = [it for it in items
            if it["kind"] == "part" or chapter_number(it["path"]) in wanted]
    return [it for i, it in enumerate(kept)
            if it["kind"] != "part"
            or (i + 1 < len(kept) and kept[i + 1]["kind"] == "chapter")]


# ---------------------------------------------------------------- summary parsing
def parse_summary() -> list[dict]:
    """Return an ordered list of items: {'kind': 'part'|'chapter', ...}."""
    items: list[dict] = []
    seen: set[Path] = set()
    section: str | None = None
    for raw in SUMMARY.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"##\s+(.*\S)", raw)
        if heading:
            section = heading.group(1).strip()
            items.append({"kind": "part", "title": section})
            continue
        # Only links inside a "Part N" section count as book chapters; links in
        # the legend, front matter or the Reference block are handled elsewhere.
        if not (section and section.lower().startswith("part")):
            continue
        for text, rel in LINK_RE.findall(raw):
            path = (ROOT / rel.replace("\\", "/")).resolve()
            if path.suffix.lower() == ".md" and path.exists() and path not in seen:
                seen.add(path)
                items.append({"kind": "chapter", "title": text.strip(), "path": path})
    return items


def parse_plan() -> list[dict]:
    """The FULL chapter plan from SUMMARY.md's part tables — including
    planned chapters that have no file yet — for the contents page."""
    plan: list[dict] = []
    section: str | None = None
    for raw in SUMMARY.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"##\s+(.*\S)", raw)
        if heading:
            section = heading.group(1).strip()
            if section.lower().startswith("part"):
                plan.append({"kind": "part", "title": section})
            continue
        if not (section and section.lower().startswith("part")):
            continue
        row = re.match(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", raw)
        if not row or row.group(1) in ("#", "---"):
            continue  # not a table row / header / separator
        num, cell, status = row.groups()
        link = LINK_RE.search(cell)
        path = (ROOT / link.group(2).replace("\\", "/")).resolve() if link else None
        plan.append({
            "kind": "chapter",
            "num": num,
            "title": link.group(1).strip() if link else cell.strip(),
            "path": path,
            "planned": status.startswith("📋"),
        })
    return plan


def contents_block(included: set[Path]) -> str:
    """A hand-built contents page: every part and chapter in the plan.

    Chapters in this build link to their heading anchor (print.css adds the
    page number); everything else is greyed out, planned chapters marked.
    Replaces Pandoc's --toc, which can only list what is in the build.
    """
    lines = ['\n\n::: {.book-toc}\n']
    for it in parse_plan():
        if it["kind"] == "part":
            lines.append(f'\n[{it["title"]}]{{.toc-part}}\n')
            continue
        num = it["num"]
        label = f'{num} — {it["title"]}' if num not in ("", "—") else it["title"]
        if it["path"] and it["path"] in included:
            lines.append(f'- [{label}](#ch-{it["path"].stem})')
        elif it["planned"]:
            lines.append(f'- [{label} · planned]{{.toc-off}}')
        else:
            lines.append(f'- [{label}]{{.toc-off}}')
    lines.append('\n:::\n')
    return "\n".join(lines)


def cover_for(path: Path) -> Path | None:
    """assets/chapter_covers/Chapter NN Cover.png for a chapter file, if present."""
    m = CHAPNUM_RE.match(path.name)
    if not m:
        return None
    cand = COVERS_DIR / f"Chapter {m.group(1)} Cover.png"
    return cand if cand.exists() else None


def part_cover_for(title: str) -> Path | None:
    """assets/chapter_covers/Part N.png for a part heading, if present."""
    m = re.match(r"Part\s+(\d+)", title)
    if not m:
        return None
    cand = COVERS_DIR / f"Part {m.group(1)}.png"
    return cand if cand.exists() else None


# ---------------------------------------------------------------- transforms
def strip_frontmatter(md: str) -> str:
    return FRONTMATTER.sub("", md, count=1)


def demote_sections(md: str) -> str:
    """Push every heading except the first H1 (the chapter title) down a level.

    Chapters use "# " for the title AND every section, which flattened the
    book's structure: the PDF TOC listed each section as if it were a
    chapter. After this pass a chapter is H1, sections are H2, subsections
    H3 — so a --toc-depth=1 TOC shows only parts and chapters. Fenced code
    blocks are skipped so `# comment` lines inside them survive.
    """
    out: list[str] = []
    in_fence = False
    title_seen = False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"#{1,5} ", line):
            if line.startswith("# ") and not title_seen:
                title_seen = True
                out.append(line)
                continue
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def render_mermaid(md: str, slug: str, enabled: bool) -> str:
    """Replace ```mermaid blocks with <img> to a pre-rendered PNG.

    PNG rather than SVG: mmdc's SVG output wraps node labels in HTML
    <foreignObject> elements, which WeasyPrint (and most EPUB readers)
    silently drop — diagrams came out as empty boxes.
    """
    if not enabled:
        return md
    mmdc = shutil.which("mmdc")
    idx = 0

    def repl(match: re.Match) -> str:
        nonlocal idx
        idx += 1
        if not mmdc:
            print(f"  ! mmdc not found — leaving diagram {slug}-{idx} as a code block")
            return match.group(0)
        MERMAID.mkdir(parents=True, exist_ok=True)
        src = MERMAID / f"{slug}-{idx}.mmd"
        out = MERMAID / f"{slug}-{idx}.png"
        src.write_text(match.group(1), encoding="utf-8")
        cmd = [mmdc, "-i", str(src), "-o", str(out), "-b", "transparent",
               "--scale", "3"]
        # Chromium refuses to sandbox as root (CI, WSL-as-root); point this at
        # a puppeteer JSON config, e.g. {"args": ["--no-sandbox"]}.
        pptr_cfg = os.environ.get("MMDC_PUPPETEER_CONFIG")
        if pptr_cfg:
            cmd += ["-p", pptr_cfg]
        subprocess.run(cmd, check=True)
        rel = out.relative_to(ROOT).as_posix()
        # Empty alt text on purpose: Pandoc turns an image with alt text that
        # stands alone in a paragraph into a captioned figure, which printed a
        # stray "Diagram" line under every diagram.
        return f'\n![]({rel}){{.mermaid-figure}}\n'

    return MERMAID_RE.sub(repl, md)


def cover_block(cover: Path) -> str:
    rel = cover.relative_to(ROOT).as_posix()
    # Raw HTML passes through Pandoc; print.css makes .chapter-cover a full page.
    return (
        f'\n\n::: {{.chapter-cover}}\n'
        f'<img src="{rel}" alt="Chapter cover"/>\n'
        f':::\n\n'
    )


# ---------------------------------------------------------------- assembly
def assemble(items: list[dict], mermaid: bool, include_glossary: bool) -> Path:
    BUILD.mkdir(parents=True, exist_ok=True)
    parts: list[str] = [f"% {TITLE}\n"]
    included = {it["path"] for it in items if it["kind"] == "chapter"}
    parts.append(contents_block(included))
    n_ch = 0
    for it in items:
        if it["kind"] == "part":
            title = it["title"]
            if title.lower().startswith("reference") and not include_glossary:
                break  # stop before the reference/back-matter section
            pcov = part_cover_for(title)
            if pcov:
                # Full-bleed part cover replaces the plain text divider; the
                # heading is kept (hidden) so the part still appears in the TOC.
                parts.append(cover_block(pcov))
                parts.append(f'\n\n::: {{.toc-only}}\n# {title}\n:::\n\n')
            else:
                parts.append(f'\n\n::: {{.part-divider}}\n# {title}\n:::\n\n')
            continue

        path: Path = it["path"]
        slug = path.stem
        md = strip_frontmatter(path.read_text(encoding="utf-8"))
        md = render_mermaid(md, slug, mermaid)
        md = demote_sections(md)
        # Tag the chapter title so print.css starts a new page there and only
        # there — otherwise every heading forced its own page. The explicit id
        # is the contents page's link target (and page-number anchor).
        md = H1_RE.sub(
            lambda m: f"# {m.group(1)} {{#ch-{slug} .chapter-title}}",
            md, count=1,
        )

        cover = cover_for(path)
        if cover:
            parts.append(cover_block(cover))
        parts.append(f'\n\n<!-- {slug} -->\n\n{md}\n')
        n_ch += 1

    if include_glossary and (ROOT / "glossary.md").exists():
        gl = strip_frontmatter((ROOT / "glossary.md").read_text(encoding="utf-8"))
        parts.append(f'\n\n::: {{.part-divider}}\n# Glossary\n:::\n\n{gl}\n')

    combined = BUILD / "combined.md"
    combined.write_text("\n".join(parts), encoding="utf-8")
    print(f"  assembled {n_ch} chapter(s) -> {combined.relative_to(ROOT)}")
    return combined


# ---------------------------------------------------------------- pandoc
def need(tool: str) -> str:
    p = shutil.which(tool)
    if not p:
        sys.exit(f"error: '{tool}' not found on PATH. See BUILD.md for install steps.")
    return p


def run(cmd: list[str]) -> None:
    print("  $", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def title_cover_args() -> list[str]:
    """--include-before-body snippet for the book title cover.

    Pandoc places include-before content ahead of the TOC, so the title
    page becomes page 1.
    """
    if not TITLE_PAGE.exists():
        return []
    rel = TITLE_PAGE.relative_to(ROOT).as_posix()
    snippet = BUILD / "title-cover.html"
    snippet.write_text(
        f'<div class="chapter-cover book-cover">'
        f'<img src="{rel}" alt="Book cover"/></div>\n',
        encoding="utf-8",
    )
    return ["--include-before-body", str(snippet.relative_to(ROOT))]


def build_pdf(combined: Path) -> None:
    need("pandoc"); need("weasyprint")
    DIST.mkdir(exist_ok=True)
    run([
        "pandoc", str(combined.relative_to(ROOT)),
        "-o", "dist/VoltForgeGear.pdf",
        "--pdf-engine=weasyprint",
        "--css", str(CSS.relative_to(ROOT)),
        # no --toc: the assembled contents page (full plan from SUMMARY.md,
        # planned chapters included) replaces Pandoc's built-chapters-only TOC.
        "--resource-path", ".",
        "--metadata", f"title={TITLE}",
    ] + title_cover_args())
    print("  -> dist/VoltForgeGear.pdf")


def build_epub(combined: Path) -> None:
    need("pandoc")
    DIST.mkdir(exist_ok=True)
    cmd = [
        "pandoc", str(combined.relative_to(ROOT)),
        "-o", "dist/VoltForgeGear.epub",
        "--toc", "--toc-depth=2",
        "--resource-path", ".",
        "--metadata", f"title={TITLE}",
    ]
    front = TITLE_PAGE if TITLE_PAGE.exists() else COVERS_DIR / "Chapter 01 Cover.png"
    if front.exists():
        cmd += ["--epub-cover-image", str(front.relative_to(ROOT))]
    run(cmd)
    print("  -> dist/VoltForgeGear.epub")


def build_html(combined: Path) -> None:
    need("pandoc")
    DIST.mkdir(exist_ok=True)
    run([
        "pandoc", str(combined.relative_to(ROOT)),
        "-o", "dist/VoltForgeGear.html",
        "--standalone",
        "--css", str(CSS.relative_to(ROOT)),
        "--resource-path", ".",
        "--metadata", f"title={TITLE}",
    ] + title_cover_args())
    print("  -> dist/VoltForgeGear.html")


# ---------------------------------------------------------------- cli
def main() -> None:
    ap = argparse.ArgumentParser(description="Build the VoltForge Gear handbook.")
    ap.add_argument("--list", action="store_true",
                    help="parse SUMMARY.md and report what was found (no external tools)")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--epub", action="store_true")
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--no-mermaid", action="store_true",
                    help="skip Mermaid pre-render (leave diagrams as code blocks)")
    ap.add_argument("--include-glossary", action="store_true",
                    help="append the glossary as back matter")
    ap.add_argument("--chapters",
                    help="comma-separated two-digit chapter numbers to build "
                         "(e.g. 00,01); default is every published chapter")
    args = ap.parse_args()

    # Windows consoles often default to cp1252, which can't print the
    # box-drawing/emoji characters used in --list output.
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not SUMMARY.exists():
        sys.exit(f"error: {SUMMARY} not found.")

    items = parse_summary()
    if args.chapters:
        wanted = {n.strip().zfill(2) for n in args.chapters.split(",") if n.strip()}
        items = filter_chapters(items, wanted)
    chapters = [i for i in items if i["kind"] == "chapter"]

    if args.list or not (args.pdf or args.epub or args.html):
        print(f"\nParsed {len(chapters)} published chapter(s) from SUMMARY.md:\n")
        cur = ""
        for it in items:
            if it["kind"] == "part":
                cur = it["title"]
                print(f"── {cur}")
            else:
                cov = cover_for(it["path"])
                tag = f"cover: {cov.name}" if cov else "cover: —"
                print(f"     • {it['path'].name:<45} {tag}")
        print(f"\n(covers found in {COVERS_DIR.relative_to(ROOT)})")
        if not args.list:
            print("\nNothing built. Pass --pdf / --epub / --html to produce output.")
        return

    combined = assemble(items, mermaid=not args.no_mermaid,
                        include_glossary=args.include_glossary)
    if args.pdf:
        build_pdf(combined)
    if args.epub:
        build_epub(combined)
    if args.html:
        build_html(combined)
    print("\nDone.")


if __name__ == "__main__":
    main()
