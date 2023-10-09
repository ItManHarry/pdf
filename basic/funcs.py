from reportlab.lib.units import inch
from reportlab.lib.colors import pink, black, red, blue, green, Color, CMYKColor, PCMYKColor
from reportlab.graphics.shapes import Rect
def coords(c):
    # c.translate(0.2*inch, 0.2*inch)
    c.setStrokeColor(pink)
    c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(black)
    c.setFont('Times-Roman', 20)
    c.drawString(0, 0, '(0, 0) the origin')
    c.drawString(2.5*inch, inch, '(2.5, 1) in inches')
    c.drawString(4*inch, 2.5*inch, '(4, 2.5)')
    c.setFillColor(red)
    c.rect(0, 2*inch, 0.2*inch, 0.3*inch, fill=1)
    c.setFillColor(green)
    c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)
def scaletranslate(c):
    c.setFont('Courier-BoldOblique', 12)
    c.saveState()
    c.scale(0.3, 0.5)
    c.translate(2.4*inch, 1.5*inch)
    c.drawString(0, 2.7*inch, 'Scale then translate')
    coords(c)
    c.restoreState()
    c.translate(2.4*inch, 1.5*inch)
    c.scale(0.3, 0.5)
    c.drawString(0, 2.7*inch, 'Translate then scale')
    coords(c)
def mirror(c):
    c.translate(5.5*inch, 0.2*inch)
    c.scale(-1, 1)
    coords(c)
def alpha(c):
    half_transparency = Color(100, 0, 0, alpha=0.5)
    c.setFillColor(black)
    c.setFont('Helvetica', 10)
    c.drawString(25, 180, 'solid')
    c.setFillColor(blue)
    c.rect(25, 25, 100, 100, fill=True, stroke=False)
    c.setFillColor(red)
    c.rect(100, 75, 100, 100, fill=True, stroke=False)
    c.setFillColor(black)
    c.drawString(225, 180, 'transparent')
    c.setFillColor(blue)
    c.rect(225, 25, 100, 100, fill=True, stroke=False)
    c.setFillColor(half_transparency)
    c.rect(300, 75, 100, 100, fill=True, stroke=False)
def colorCMYK(canvas):
    black = CMYKColor(0, 0, 0, 1)
    cyan = PCMYKColor(100, 0, 0, 0)
    x = y = 0
    dy = 3 * inch / 4.0
    dx = 5.5 * inch / 5
    w = h = dy / 2
    rdx = (dx - w) / 2
    rdy = h / 5.0
    texty = h + 2 * rdy
    canvas.setFont('Helvetica', 10)
    y = y + dy
    x = 0
    for cmyk in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0)]:
        c, m, y1, k = cmyk
        canvas.setFillColorCMYK(c, m, y1, k)
        canvas.rect(x+rdx, y+rdy, w, h, fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+dx/2, y+texty, f'c{c} m{m} y{y1} k{k}')
        x += dx