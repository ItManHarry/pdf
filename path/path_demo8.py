'''
Bezier Demo 2
'''
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import yellow, red, green, black
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def bezier(c):
    xd, yd = 5.5*inch/2, 3*inch/2
    xc, yc = xd, yd
    dxdy = [(0, 0.33), (0.33, 0.33), (0.75, 1), (0.875, 0.875), (0.875, 0.875), (1, 0.75), (0.33, 0.33), (0.33, 0)]
    points = []
    for x_offset in (1, -1):
        y_offset = x_offset
        for dx, dy in dxdy:
            px = xc + xd*x_offset*dx
            py = yc + yd*y_offset*dy
            points.append((px, py))
        y_offset = -x_offset
        for dy, dx in dxdy:
            px = xc + xd*x_offset*dx
            py = yc + yd*y_offset*dy
            points.append((px, py))
    c.setLineWidth(0.1*inch)
    while points:
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = points[:4]
        del points[:4]
        print(f'[x1: {x1}, y1: {y1}] [x2: {x2}, y2: {y2}] [x3: {x3}, y1: {y3}] [x4: {x4}, y4: {y4}]')
        c.setLineWidth(0.1*inch)
        c.setStrokeColor(green)
        c.line(x1, y1, x2, y2)
        c.setStrokeColor(red)
        c.line(x3, y3, x4, y4)
        c.setStrokeColor(black)
        c.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
c = canvas.Canvas('path_demo8.pdf')
bezier(c)
c.showPage()
c.save()