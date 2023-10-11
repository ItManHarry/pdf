import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from path_demo1 import star
os.chdir(r'd:\python\pdf')
def caps(cv):
    cv.setLineWidth(5)
    star(cv, 'Default', 'no projection', x_center=1*inch, vertices=4)
    cv.setLineCap(1)
    star(cv, 'Round cap', '1: ends in half circle', vertices=4)
    cv.setLineCap(2)
    star(cv, 'Square cap', '2: projects out half a width', x_center=4.5*inch, vertices=4)
cv = canvas.Canvas('path_demo3.pdf')
caps(cv)
cv.showPage()
cv.save()