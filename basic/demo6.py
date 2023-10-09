from reportlab.pdfgen import canvas
import os
from funcs import scaletranslate
os.chdir(r'D:\Python\pdf')
c = canvas.Canvas('demo6.pdf')
scaletranslate(c)
c.showPage()
c.save()