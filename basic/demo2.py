import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
def gen_pdf(c):
    c.setStrokeColorRGB(1, 0, 0)
    c.line(0, 0, 0, 1.7 * inch)
    c.line(0, 0, 1 * inch, 0)
    c.translate(inch, inch)
    # c.setFillColorRGB(1, 0, 0)
    c.setStrokeColorRGB(0, 1, 0)
    c.line(0, 0, 0, 1.7 * inch)
    c.line(0, 0, 1 * inch, 0)
    c.translate(0.2*inch, 0.2*inch)
    c.setStrokeColorRGB(0, 0, 1)
    c.setFillColorRGB(0.2, 0.5, 0.6)
    c.rect(0, 0, inch, 1.5*inch, fill=0)
    c.translate(3*inch, 0.5*inch)
    c.rotate(90)
    c.setStrokeColorRGB(1, 0, 0)
    c.line(0, 0, 0, 4*inch)
    c.setStrokeColorRGB(0, 0, 1)
    c.line(0, 0, 4*inch, 0)
    c.setStrokeColorRGB(0, 1, 0)
    c.line(0, 4*inch, 4*inch, 0)
    c.setStrokeColorRGB(1, 0, 0)
    c.line(0, -4 * inch, 0, 0)
    c.line(0, -4 * inch, 4 * inch, 0)
os.chdir(r'D:\Python\pdf')
c = canvas.Canvas('demo2.pdf')
gen_pdf(c)
c.showPage()
c.save()