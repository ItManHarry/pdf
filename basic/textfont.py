import os
from reportlab.pdfgen import canvas
from funcs import text_font
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('textfont.pdf')
text_font(cv)
cv.showPage()
cv.save()