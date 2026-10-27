#!/usr/bin/env python3
"""
md2pdf.py -- render a markdown file to PDF.

    venv\\Scripts\\python.exe md2pdf.py README.md DSA301-Editor-Guide.pdf

Needs reportlab:  venv\\Scripts\\python.exe -m pip install reportlab

Handles the markdown these docs use: headings, paragraphs, bullet and numbered
lists, fenced code, tables, blockquotes, rules, and inline bold / `code`.

GLYPH NOTE: reportlab's built-in fonts use WinAnsi encoding and cannot draw
arrows, box-drawing characters, dashes or smart quotes -- those come out as solid
blocks or question marks. Everything outside plain Latin-1 is transliterated to
ASCII before rendering. Do not remove that step.
"""

import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, ListFlowable, ListItem, Paragraph,
                                Preformatted, SimpleDocTemplate, Spacer, Table,
                                TableStyle)

TRANSLITERATE = {
    "→": "->", "←": "<-", "↔": "<->", "⇒": "=>",
    "≥": ">=", "≤": "<=", "≠": "!=", "×": "x",
    "✅": "[ok]", "❌": "[x]", "⚠": "[!]", "✓": "[y]",
    "✗": "[n]", "•": "-", "●": "-", "▪": "-",
    "├": "+", "└": "+", "│": "|", "─": "-",
    "┬": "+", "┴": "+", "┼": "+", "┐": "+",
    "┌": "+", "┘": "+", "…": "...",
    "—": " - ", "–": "-", "‑": "-", "―": "-",
    "‘": "'", "’": "'", "“": '"', "”": '"',
    " ": " ", " ": " ", " ": " ", "​": "",
    "−": "-", "·": "-", "�": "-", "′": "'", "″": '"',
}


def deglyph(s):
    for bad, good in TRANSLITERATE.items():
        s = s.replace(bad, good)
    return s.encode("latin-1", "replace").decode("latin-1")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s):
    s = esc(deglyph(s))
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+?)`",
               r'<font face="Courier" size="8.5" color="#9d174d">\1</font>', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    return s


def styles():
    getSampleStyleSheet()
    base = dict(fontName="Helvetica", fontSize=9.6, leading=14.2,
                textColor=colors.HexColor("#1f2328"), alignment=TA_LEFT)
    return {
        "title": ParagraphStyle("t", **dict(base, fontName="Helvetica-Bold",
                                            fontSize=21, leading=26, spaceAfter=2,
                                            textColor=colors.HexColor("#0b3d63"))),
        "h1": ParagraphStyle("h1", **dict(base, fontName="Helvetica-Bold",
                                          fontSize=15, leading=19, spaceBefore=17,
                                          spaceAfter=6,
                                          textColor=colors.HexColor("#0b3d63"))),
        "h2": ParagraphStyle("h2", **dict(base, fontName="Helvetica-Bold",
                                          fontSize=11.6, leading=15, spaceBefore=12,
                                          spaceAfter=4,
                                          textColor=colors.HexColor("#14507d"))),
        "h3": ParagraphStyle("h3", **dict(base, fontName="Helvetica-Bold",
                                          fontSize=10.2, leading=13.5,
                                          spaceBefore=9, spaceAfter=3)),
        "body": ParagraphStyle("b", **dict(base, spaceAfter=6)),
        "quote": ParagraphStyle("q", **dict(base, leftIndent=10, spaceAfter=7,
                                            borderPadding=(5, 5, 5, 5),
                                            backColor=colors.HexColor("#fff8e6"),
                                            textColor=colors.HexColor("#5c4a03"))),
        "li": ParagraphStyle("li", **dict(base, spaceAfter=2.5)),
        "code": ParagraphStyle("c", fontName="Courier", fontSize=7.6, leading=9.9,
                               textColor=colors.HexColor("#0f2b3d")),
        "th": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.4,
                             leading=11, textColor=colors.white),
        "td": ParagraphStyle("td", fontName="Helvetica", fontSize=8.4, leading=11,
                             textColor=colors.HexColor("#1f2328")),
    }


def wrap_code(lines, width=104):
    out = []
    for ln in lines:
        ln = deglyph(ln.rstrip("\n")).replace("\t", "    ")
        while len(ln) > width:
            out.append(ln[:width])
            ln = "    " + ln[width:]
        out.append(ln)
    return out


def code_block(lines, st, avail):
    t = Table([[Preformatted("\n".join(wrap_code(lines)) or " ", st["code"])]],
              colWidths=[avail])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f2f6f9")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#ccd7e0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def make_table(rs, st, avail):
    header, body = rs[0], rs[1:]
    ncols = max(len(r) for r in rs)
    header = header + [""] * (ncols - len(header))
    body = [r + [""] * (ncols - len(r)) for r in body]

    weights = []
    for i in range(ncols):
        longest = max([len(header[i])] + [len(r[i]) for r in body] or [1])
        weights.append(max(6, min(longest, 60)))
    total = float(sum(weights))
    widths = [avail * w / total for w in weights]

    data = [[Paragraph(inline(c), st["th"]) for c in header]]
    for r in body:
        data.append([Paragraph(inline(c), st["td"]) for c in r])

    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#14507d")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#f4f7fa")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c7d2dc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def convert(md_path, pdf_path):
    lines = open(md_path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    st = styles()
    margin = 17 * mm
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=margin, rightMargin=margin,
                            topMargin=15 * mm, bottomMargin=15 * mm,
                            title=os.path.splitext(os.path.basename(pdf_path))[0],
                            author="DSA-301 editor")
    avail = doc.width
    flow, i, para, bullets, numbers = [], 0, [], [], []

    def flush_para():
        if para:
            flow.append(Paragraph(inline(" ".join(para)), st["body"]))
            del para[:]

    def flush_lists():
        for store, kind in ((bullets, "bullet"), (numbers, "1")):
            if store:
                flow.append(ListFlowable(
                    [ListItem(Paragraph(inline(x), st["li"]), leftIndent=13)
                     for x in store],
                    bulletType=kind, start="1" if kind == "1" else None,
                    leftIndent=13, bulletFontSize=8.6,
                    bulletColor=colors.HexColor("#14507d")))
                flow.append(Spacer(1, 4))
                del store[:]

    def flush_all():
        flush_para()
        flush_lists()

    while i < len(lines):
        line = lines[i].rstrip()

        if line.lstrip().startswith("```"):
            flush_all()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            flow.append(code_block(buf, st, avail))
            flow.append(Spacer(1, 7))
            continue

        if line.strip().startswith("|") and "|" in line.strip()[1:]:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if re.match(r"^\s*\|?[\s:*-]*-[-\s:|]*\|?\s*$", nxt):
                flush_all()
                rs = [split_row(line)]
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    rs.append(split_row(lines[i]))
                    i += 1
                flow.append(make_table(rs, st, avail))
                flow.append(Spacer(1, 8))
                continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_all()
            level, text = len(m.group(1)), m.group(2)
            if level == 1 and not flow:
                flow.append(Paragraph(inline(text), st["title"]))
                flow.append(HRFlowable(width="100%", thickness=1.1,
                                       color=colors.HexColor("#0b3d63"),
                                       spaceBefore=4, spaceAfter=9))
            else:
                key = "h1" if level <= 2 else ("h2" if level == 3 else "h3")
                flow.append(Paragraph(inline(text), st[key]))
                if level <= 2:
                    flow.append(HRFlowable(width="100%", thickness=0.5,
                                           color=colors.HexColor("#c7d2dc"),
                                           spaceBefore=1, spaceAfter=7))
            i += 1
            continue

        if re.match(r"^\s*([-*_])\s*(\1\s*){2,}$", line):
            flush_all()
            flow.append(Spacer(1, 3))
            i += 1
            continue

        if line.lstrip().startswith(">"):
            flush_all()
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip())
                i += 1
            flow.append(Paragraph(inline(" ".join(buf)), st["quote"]))
            continue

        mb = re.match(r"^\s*[-*+]\s+(.*)$", line)
        mn = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if mb:
            flush_para()
            if numbers:
                flush_lists()
            bullets.append(mb.group(1))
            i += 1
            continue
        if mn:
            flush_para()
            if bullets:
                flush_lists()
            numbers.append(mn.group(1))
            i += 1
            continue

        if (bullets or numbers) and line.startswith(("  ", "\t")) and line.strip():
            (bullets if bullets else numbers)[-1] += " " + line.strip()
            i += 1
            continue

        if not line.strip():
            flush_all()
            i += 1
            continue

        flush_lists()
        para.append(line.strip())
        i += 1

    flush_all()

    def footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.4)
        canvas.setFillColor(colors.HexColor("#8b949e"))
        canvas.drawString(margin, 9 * mm, "DSA-301 HackerRank Challenge Editor")
        canvas.drawRightString(A4[0] - margin, 9 * mm, "Page %d" % doc_.page)
        canvas.restoreState()

    doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    return pdf_path


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    src = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    dst = sys.argv[2] if len(sys.argv) > 2 else "DSA301-Editor-Guide.pdf"
    if not os.path.isabs(src):
        src = os.path.join(here, src)
    if not os.path.isabs(dst):
        dst = os.path.join(here, dst)
    out = convert(src, dst)
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))
