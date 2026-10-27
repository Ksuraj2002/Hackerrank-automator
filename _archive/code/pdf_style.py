# -*- coding: utf-8 -*-
r"""Shared page furniture for the PDFs this project generates.

Kept in one place so make_gaps_pdf.py and any future report look like the same
document rather than two documents that happen to be about the same thing.

One hard constraint: reportlab's built-in fonts carry no glyphs for arrows, check
marks or maths symbols, and a missing glyph renders as a solid black box. Text
passed to these helpers must stay within WinAnsi. Em dashes, en dashes, curly
quotes and bullets are all fine; anything more exotic is not.
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

INK = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#5b6470")
ACCENT = colors.HexColor("#1f6feb")
RULE = colors.HexColor("#d7dce2")
CODE_BG = colors.HexColor("#f4f6f8")
CODE_INK = colors.HexColor("#10243e")
WARN_BG = colors.HexColor("#fff8e6")
WARN_EDGE = colors.HexColor("#e0b34d")
NOTE_BG = colors.HexColor("#eef4ff")
NOTE_EDGE = colors.HexColor("#9dc0f5")
HEAD_BG = colors.HexColor("#33415a")
ZEBRA = colors.HexColor("#fafbfc")

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

_ss = getSampleStyleSheet()


def style(name, **kw):
    base = kw.pop("parent", _ss["BodyText"])
    return ParagraphStyle(name, parent=base, **kw)


H1 = style("H1", fontName="Helvetica-Bold", fontSize=21, leading=25,
           textColor=INK, spaceBefore=0, spaceAfter=3)
SUB = style("SUB", fontName="Helvetica", fontSize=10.5, leading=14,
            textColor=MUTED, spaceAfter=14)
H2 = style("H2", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
           textColor=INK, spaceBefore=18, spaceAfter=5, keepWithNext=1)
H3 = style("H3", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
           textColor=INK, spaceBefore=10, spaceAfter=3, keepWithNext=1)
BODY = style("BODY", fontName="Helvetica", fontSize=9.7, leading=14,
             textColor=INK, alignment=TA_LEFT, spaceAfter=7)
SMALL = style("SMALL", fontName="Helvetica", fontSize=8.5, leading=12,
              textColor=MUTED, spaceAfter=6)
TH = style("TH", fontName="Helvetica-Bold", fontSize=8.3, leading=11,
           textColor=colors.white, spaceAfter=0)
TD = style("TD", fontName="Helvetica", fontSize=8.3, leading=11,
           textColor=INK, spaceAfter=0)
TD_MONO = style("TD_MONO", fontName="Courier", fontSize=7.9, leading=11,
                textColor=CODE_INK, spaceAfter=0)


def mono(t):
    return '<font face="Courier" color="#10243e">%s</font>' % t


def xml_escape(t):
    """Make free text safe inside a reportlab Paragraph."""
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def rule(color=ACCENT, height=1):
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[height])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color)]))
    return t


def callout(title, body, bg=WARN_BG, edge=WARN_EDGE):
    inner = [
        Paragraph(title, style("CO_T", fontName="Helvetica-Bold", fontSize=9.3,
                               leading=12.5, textColor=INK, spaceAfter=3)),
        Paragraph(body, style("CO_B", fontName="Helvetica", fontSize=9.1,
                              leading=13, textColor=INK, spaceAfter=0)),
    ]
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.7, edge),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return [Spacer(1, 3), KeepTogether(t), Spacer(1, 10)]


def table(headers, rows, widths, mono_cols=(), align_right=()):
    """A zebra-striped table whose header repeats across page breaks."""
    data = [[Paragraph(h, TH) for h in headers]]
    for r in rows:
        data.append([
            Paragraph(c, TD_MONO if i in mono_cols else TD)
            for i, c in enumerate(r)
        ])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
        ("BOX", (0, 0), (-1, -1), 0.6, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    for c in align_right:
        st.append(("ALIGN", (c, 1), (c, -1), "RIGHT"))
    t.setStyle(TableStyle(st))
    return [Spacer(1, 3), t, Spacer(1, 10)]


def numbered_heading(n, title, *companions):
    """A heading with a filled badge, pinned to the content that follows it."""
    badge = Table([[Paragraph(
        "<b>%s</b>" % n,
        style("BG", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
              textColor=colors.white, alignment=1))]],
        colWidths=[7.4 * mm], rowHeights=[7.4 * mm])
    badge.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    row = Table([[badge, Paragraph(title, style(
        "SECT", fontName="Helvetica-Bold", fontSize=12.5, leading=15.5,
        textColor=INK, spaceAfter=0))]],
        colWidths=[10.2 * mm, CONTENT_W - 10.2 * mm])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    pinned = [row, Spacer(1, 5)]
    for c in companions:
        pinned.extend(c if isinstance(c, list) else [c])
    return [Spacer(1, 13), KeepTogether(pinned)]


def build(path, story, footer_text, title, subject=""):
    """Render `story` to `path` with a footer and page numbers."""
    def on_page(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7.5)
        canv.setFillColor(MUTED)
        canv.drawString(MARGIN, 10 * mm, footer_text)
        canv.drawRightString(PAGE_W - MARGIN, 10 * mm, "Page %d" % canv.getPageNumber())
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.5)
        canv.line(MARGIN, 13.5 * mm, PAGE_W - MARGIN, 13.5 * mm)
        canv.restoreState()

    doc = BaseDocTemplate(
        str(path), pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=16 * mm, bottomMargin=18 * mm,
        title=title, subject=subject,
    )
    frame = Frame(MARGIN, 18 * mm, CONTENT_W, PAGE_H - 16 * mm - 18 * mm, id="body")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=on_page)])
    doc.build(story)
    return path
