import os
from reportlab.pdfgen import canvas
from path_demo5 import penciltip
from reportlab.lib.units import inch
from reportlab.lib.colors import yellow, red, black, white
os.chdir(r'd:\python\pdf')
def pencil(cv, text='No. 2'):
    u = inch / 10
    cv.setStrokeColor(black)
    cv.setLineWidth(4)
    cv.setFillColor(red)
    cv.circle(30 * u, 5 * u, 5 * u, stroke=1, fill=1)
    cv.setFillColor(yellow)
    cv.rect(10 * u, 0, 20 * u, 10 * u, stroke=1, fill=1)
    cv.setFillColor(black)
    cv.rect(23 * u, 0, 8 * u, 10 * u, stroke=1, fill=1)
    cv.roundRect(14 * u, 3.5 * u, 8 * u, 3 * u, 1.5 * u, stroke=1, fill=1)
    cv.setFillColor(white)
    cv.rect(25 * u, u, 1.2 * u, 8 * u, fill=1, stroke=0)
    cv.rect(27.5 * u, u, 1.2 * u, 8 * u, fill=1, stroke=0)
    cv.setFont('Times-Roman', 3 * u)
    cv.drawCentredString(18 * u, 4 * u, text)
    penciltip(cv, debug=0)
    cv.setDash([10, 5, 16, 10], 0)
    cv.line(11 * u, 2.5 * u, 22 * u, 2.5 * u)
    cv.line(22 * u, 7.5 * u, 12 * u, 7.5 * u)
cv = canvas.Canvas('path_demo6.pdf')
pencil(cv)
cv.showPage()
cv.save()