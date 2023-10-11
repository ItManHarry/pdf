import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from path_demo1 import star
os.chdir(r'd:\python\pdf')
def dashes(cv):
    cv.setDash(6, 3)
    star(cv, 'Simple dashes', '6 points on, 3 off', x_center=1*inch)
    cv.setDash(1, 2)
    star(cv, 'Dots', 'One on, two off')
    cv.setDash([1, 1, 3, 3, 4, 4, 1], 0)
    star(cv, 'Complex Pattern', '[1, 1, 3, 3, 4, 4, 1]', x_center=4.5*inch)
cv = canvas.Canvas('path_demo4.pdf')
dashes(cv)
cv.showPage()
cv.save()