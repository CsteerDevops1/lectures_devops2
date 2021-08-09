#!/usr/bin/env python3

"""
Формат PDF: библиотека reportlab
"""

from reportlab.lib.colors import Color, black, blue, red
from reportlab.pdfgen import canvas


def hello(c):
    c.drawString(100, 100, "Hello World")


def alpha(canvas):
    red50transparent = Color(100, 0, 0, alpha=0.5)
    c = canvas
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(25, 180, "solid")
    c.setFillColor(blue)
    c.rect(25, 25, 100, 100, fill=True, stroke=False)
    c.setFillColor(red)
    c.rect(100, 75, 100, 100, fill=True, stroke=False)
    c.setFillColor(black)
    c.drawString(225, 180, "transparent")
    c.setFillColor(blue)
    c.rect(225, 25, 100, 100, fill=True, stroke=False)
    c.setFillColor(red50transparent)
    c.rect(300, 75, 100, 100, fill=True, stroke=False)


text_pdf = canvas.Canvas("text.pdf")
hello(text_pdf)
text_pdf.showPage()
text_pdf.save()

canvas_pdf = canvas.Canvas("canvas.pdf")
alpha(canvas_pdf)
canvas_pdf.showPage()
canvas_pdf.save()
