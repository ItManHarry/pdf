import os
from reportlab.pdfgen import canvas
from funcs import mirror
os.chdir(r'd:\python\pdf')
c = canvas.Canvas('demo7.pdf')
mirror(c)
c.showPage()
c.save()