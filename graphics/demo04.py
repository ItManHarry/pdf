from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart, VerticalBarChart3D
import os
os.chdir(r'd:\python\pdf')
d = Drawing()
data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (14, 6, 21, 23, 38, 46, 20, 5),
]
b = VerticalBarChart()
b.x = 50
b.y = 50
b.height = 125
b.width = 300
b.data = data
b.strokeColor = colors.black
b.valueAxis.valueMin = 0
b.valueAxis._valueMax = 50
b.valueAxis.valueStep = 10
b.categoryAxis.labels.boxAnchor = 'ne'
b.categoryAxis.labels.dx = 8
b.categoryAxis.labels.dy = -2
b.categoryAxis.labels.angle = 30
b.groupSpacing = 10
b.barSpacing = 2.5
b.categoryAxis.categoryNames = ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', '', '']
d.add(b)
renderPDF.drawToFile(d, 'demo04.pdf')