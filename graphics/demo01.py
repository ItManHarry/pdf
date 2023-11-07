import os
from reportlab.graphics.charts.piecharts import Pie
os.chdir(r'd:\python\pdf')
from reportlab.lib import colors
from reportlab.graphics.shapes import *
d = Drawing(500, 300)
d.add(Rect(50, 50, 400, 100, fillColor=colors.yellow))
d.add(String(150, 100, 'Hello ReportLab Graphics', fontSize=18, fillColor=colors.red))
d.add(String(180, 86, 'Special characters \\xc2\xa2\xc2\xa9\xc2\xae\xc2\xa3\xce\xb1\xce\xb2', fillColor=colors.red))
pc = Pie()
pc.x = 50
pc.y = 180
pc.data = [10, 20, 30, 40, 50, 60]
pc.labels = ['a', 'b', 'c', 'd', 'e', 'f']
pc.slices.strokeWidth = 0.5
pc.slices[3].popout = 20
pc.slices[3].strokeWidth = 2
pc.slices[3].strokeDashArray = [2, 2]
pc.slices[3].labelRadius = 1.75
pc.slices[3].fontColor = colors.red
d.add(pc, '')
from reportlab.graphics import renderPDF, renderPS, renderPM, renderSVG
# renderPDF.drawToFile(d, 'demo01.pdf', 'My First Drawing')
# renderPS.drawToFile(d, 'demo01.eps')
# renderPM.drawToFile(d, 'demo01.png', 'PNG')
renderSVG.drawToFile(d, 'demo01.svg')