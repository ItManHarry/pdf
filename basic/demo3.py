import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'D:\Python\pdf')
c = canvas.Canvas('demo3.pdf')
c.translate(inch, inch)
c.setStrokeColorRGB(1, 0, 0)
c.line(0, 0, inch, 0)
c.translate(0.1*inch, 0.1*inch)
c.setStrokeColorRGB(0, 1, 0)
c.rect(0, 0, 2*inch, inch)
c.arc(0, 0, 1*inch, 1.5*inch)
c.ellipse(0, 0, 1*inch, 1.5*inch)
c.line(0, 0, 1*inch, 1.5*inch)
c.bezier(0, 0, inch, inch, 1.5*inch, 1.5*inch, 2*inch, 2*inch)
c.translate(inch, inch)
c.circle(0, 0, inch)
c.translate(inch, inch)
c.roundRect(0, 0, 1.5*inch, inch, 30)
c.translate(0, 2*inch)
c.line(0, 0, 2*inch, 0)
c.drawString(0, 0, 'It is OK!')
c.line(0, inch, 2*inch, inch)
c.drawRightString(0, inch, 'Right String!')
c.line(0, 1.5*inch, 2*inch, 1.5*inch)
c.drawCentredString(0, 1.5*inch, 'Centered String!')
c.showPage()
c.save()