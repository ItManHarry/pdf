import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
d = Drawing()
data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (5, 20, 46, 38, 23, 21, 6, 14)
]
l = HorizontalLineChart()
l.x = 50
l.y = 50
l.height = 125
l.width = 300
l.data = data
l.joinedLines = 1
cns = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug'.split(',')
l.categoryAxis.categoryNames = cns
l.categoryAxis.labels.boxAnchor = 'n'
l.valueAxis.valueMin = 0
l.valueAxis.valueMax = 60
# l.valueAxis.ValueStep = 15
l.lines[0].strokeWidth = 2
l.lines[1].strokeWidth = 1.5
d.add(l)
from reportlab.graphics import renderPDF
renderPDF.drawToFile(d, 'demo05.pdf')