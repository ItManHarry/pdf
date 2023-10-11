import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def star(cv, title='Title Here', comment='Comment here', x_center=None, y_center=None, vertices=5):
    radius = inch / 3.0
    if x_center is None:
        x_center = 2.75*inch
    if y_center is None:
        y_center = 1.5*inch
    cv.drawCentredString(x_center, y_center+1.3*inch, title)
    cv.drawCentredString(x_center, y_center-1.4*inch, comment)
    p = cv.beginPath()
    p.moveTo(x_center, y_center+radius)
    from math import pi, cos, sin
    print('PI is : ', pi)
    angle = (2*pi)*2/5.0
    start_angle = pi/2.0
    for vertex in range(vertices-1):
        next_angle = angle*(vertex+1)+start_angle
        x = x_center + radius*cos(next_angle)
        y = y_center + radius*sin(next_angle)
        p.lineTo(x, y)
    if vertices == 5:
        p.close()
    cv.drawPath(p)
cv = canvas.Canvas('path_demo1.pdf')
star(cv)
cv.showPage()
cv.save()