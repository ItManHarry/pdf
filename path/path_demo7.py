'''
Bezier Line Demo 1
'''
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import yellow, red, black, green
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def bizier(c):
    i = inch
    d = i / 4
    x1, y1, x2, y2, x3, y3, x4, y4 = d, 1.5*i, 1.5*i, d, 3*i, d, 5.5*i-d, 3*i-d
    print(f'[x1: {x1}, y1: {y1}] [x2: {x2}, y2: {y2}] [x3: {x3}, y1: {y3}] [x4: {x4}, y4: {y4}]')
    c.setFillColor(yellow)
    p = c.beginPath()
    p.moveTo(x1, y1)
    for x, y in [(x2, y2), (x3, y3), (x4, y4)]:
        p.lineTo(x, y)
    c.drawPath(p, fill=1, stroke=0)
    c.setLineWidth(0.1*i)
    c.setStrokeColor(green)
    c.line(x1, y1, x2, y2)
    c.setStrokeColor(red)
    c.line(x3, y3, x4, y4)
    c.setStrokeColor(black)
    c.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
c = canvas.Canvas('path_demo7.pdf')
bizier(c)
c.showPage()
c.save()