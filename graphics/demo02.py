import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib import colors
d = shapes.Drawing(200, 100)
d.add(shapes.Circle(100, 90, 5, fillColor=colors.green))
l = Label()
l.setOrigin(100, 90)
l.boxAnchor = 'ne'
l.angle = 45
l.dx = 0
l.dy = -20
l.boxStrokeColor = colors.green
l.setText('Some \nMulti-Line \nLabel')
d.add(l)
from reportlab.graphics import renderPDF
renderPDF.drawToFile(d, 'demo02.pdf', 'My Second PDF File.')