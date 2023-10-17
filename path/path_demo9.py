'''
arc shape
'''
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def arcs(c):
    c.setLineWidth(4)
    c.setStrokeColorRGB(0.8, 1, 0.6)
    c.rect(inch, inch, 1.5*inch, 1.5*inch)
    # c.rect(inch, inch, 2.5 * inch, 2 * inch)
    c.rect(3*inch, inch, inch, 1.5*inch)
    c.setStrokeColorRGB(0, 0.2, 0.4)
    c.setFillColorRGB(1, 0.6, 0.8)
    # c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(0.2*inch, 0.2*inch)
    # p.rect(inch, inch, 2.5*inch, 2*inch)
    p.arcTo(inch, inch, 2.5*inch, 2*inch, startAng=-30, extent=135)
    p.arc(3*inch, inch, 4*inch, 2.5*inch, startAng=-45, extent=270)
    c.drawPath(p, fill=1, stroke=1)
c = canvas.Canvas('path_demo9_4.pdf')
arcs(c)
c.showPage()
c.save()