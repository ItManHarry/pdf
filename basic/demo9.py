import os
from reportlab.pdfgen import canvas
from funcs import colorCMYK
os.chdir(r'd:\python\pdf')
c = canvas.Canvas('demo9.pdf')
colorCMYK(c)
c.showPage()
c.save()