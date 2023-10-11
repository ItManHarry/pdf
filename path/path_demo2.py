import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from path_demo1 import star
os.chdir(r'd:\python\pdf')
def joins(cv):
    cv.setLineWidth(5)
    star(cv, 'Default: mitered join', '0: pointed', x_center=1*inch)
    cv.setLineJoin(1)
    star(cv, 'Round join', '1: rounded')
    cv.setLineJoin(2)
    star(cv, 'Bevelled join', '2: square', x_center=4.5*inch)
cv = canvas.Canvas('path_demo2.pdf')
joins(cv)
cv.showPage()
cv.save()