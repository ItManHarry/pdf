'''
path various shapes
'''
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def various_shapes(c):
    c.setStrokeGray(0.5)
    c.grid(range(0, int(11*inch/2), int(inch/2)), range(0, int(7*inch/2), int(inch/2)))
    c.setLineWidth(4)
    c.setStrokeColorRGB(0, 0.2, 0.7)
    c.setFillColorRGB(1, 0.6, 0.8)
    p = c.beginPath()
    p.rect(0.5*inch, 0.5*inch, 0.5*inch, 2*inch)
    p.circle(2.75*inch, 1.5*inch, 0.3*inch)
    p.ellipse(3.5*inch, 0.5*inch, 1.2*inch, 2*inch)
    c.drawPath(p, fill=1, stroke=1)
c = canvas.Canvas('path_demo10.pdf')
various_shapes(c)
c.showPage()
c.save()