import os
from reportlab.pdfgen import canvas
from funcs import spumoni2
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('demo11.pdf')
spumoni2(cv)
cv.showPage()
cv.save()