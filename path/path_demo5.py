import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import tan, black, green
os.chdir(r'd:\python\pdf')
def penciltip(cv, debug=1):
    u = inch / 10
    cv.setLineWidth(4)
    if debug:
        cv.scale(2.8, 2.8)
        cv.setLineWidth(1)
    cv.setStrokeColor(black)
    cv.setFillColor(tan)
    p = cv.beginPath()
    p.moveTo(10 * u, 0)
    p.lineTo(0, 5 * u)
    p.lineTo(10 * u, 10 * u)
    p.curveTo(11.5 * u, 10 * u, 11.5 * u, 7.5 * u, 10 * u, 7.5 * u)
    p.curveTo(12 * u, 7.5 * u, 11 * u, 2.5 * u, 9.7 * u, 2.5 * u)
    p.curveTo(10.5 * u, 2.5 * u, 11 * u, 0, 10 * u, 0)
    cv.drawPath(p, stroke=1, fill=1)
    cv.setFillColor(black)
    # cv.setStrokeColor(red)
    p = cv.beginPath()
    p.moveTo(0, 5 * u)
    p.lineTo(4 * u, 3 * u)
    p.lineTo(5 * u, 4.5 * u)
    p.lineTo(3 * u, 6.5 * u)
    cv.drawPath(p, stroke=1, fill=1)
    if debug:
        cv.setStrokeColor(green)
        cv.grid([0, 5 * u, 10 * u, 15 * u], [0, 5 * u, 10 * u])
cv = canvas.Canvas('path_demo5.pdf')
penciltip(cv)
cv.showPage()
cv.save()