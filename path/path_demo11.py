'''
path object close
'''
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def close_figures(c):
    h, k = inch/3, inch/2
    c.setStrokeColorRGB(0.2, 0.3, 0.5)
    c.setFillColorRGB(0.8, 0.6, 0.2)
    c.setLineWidth(4)
    p = c.beginPath()
    for i in (1, 2, 3, 4):
        for j in (1, 2):
            xc, yc = inch*i, inch*j
            p.moveTo(xc, yc)
            p.arcTo(xc-h, yc-k, xc+h, yc+k, startAng=0, extent=60*i)
            if j == 1:
                p.close()
    c.drawPath(p, fill=1, stroke=1)
c = canvas.Canvas('path_demo11.pdf')
close_figures(c)
c.showPage()
c.save()