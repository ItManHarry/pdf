import os
from reportlab.pdfgen import canvas
from funcs import text_size
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('textsize.pdf')
text_size(cv)
cv.showPage()
cv.save()