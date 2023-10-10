import os
from reportlab.pdfgen import canvas
from funcs import spumoni
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('demo10.pdf')
spumoni(cv)
cv.showPage()
cv.save()