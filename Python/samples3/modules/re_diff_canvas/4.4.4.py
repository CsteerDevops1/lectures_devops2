# -*- encoding: utf-8 -*-
"""
Формат PDF: библиотека reportlab
"""
from reportlab.pdfgen import canvas

def hello(c):
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()

c = canvas.Canvas("hello.pdf")
def alpha(canvas):
    from reportlab.graphics.shapes import Rect
    from reportlab.lib.colors import Color, black, blue, red
    red50transparent = Color( 100, 0, 0, alpha=0.5)
    c = canvas
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(25,180, 'solid')
    c.setFillColor(blue)
    c.rect(25,25,100,100, fill=True, stroke=False)
    c.setFillColor(red)
    c.rect(100,75,100,100, fill=True, stroke=False)
    c.setFillColor(black)
    c.drawString(225,180, 'transparent')
    c.setFillColor(blue)
    c.rect(225,25,100,100, fill=True, stroke=False)
    c.setFillColor(red50transparent)
    c.rect(300,75,100,100, fill=True, stroke=False)

alpha(c)
c.showPage()
c.save()
