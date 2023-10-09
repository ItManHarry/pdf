import os
from reportlab.pdfgen import canvas
from funcs import alpha
os.chdir(r'd:\python\pdf')
c = canvas.Canvas('demo8.pdf')
alpha(c)
c.showPage()
c.save()