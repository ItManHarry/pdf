from reportlab.pdfgen import canvas
import os
from funcs import coords
from reportlab.lib.units import inch
os.chdir(r'D:\Python\pdf')
c = canvas.Canvas('demo5.pdf')
c.translate(0.5*inch, 0.5*inch)
coords(c)
c.showPage()
c.save()