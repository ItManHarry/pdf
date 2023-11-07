import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
d = Drawing()
data = [
    ((1, 1), (2, 2), (2.5, 1), (3, 3), (4, 5)),
    ((1, 2), (2, 3), (2.5, 2), (3.5, 5), (4, 6)),
]
l = LinePlot()
l.x = 50
l.y = 50
l.height = 125
l.width = 300
l.data = data
l.joinedLines = 1
l.lines[0].symbol = makeMarker('FilledCircle')
l.lines[1].symbol = makeMarker('Circle')
l.lineLabelFormat = '%2.0f'
l.strokeColor = colors.black
l.xValueAxis.valueMin = 0
l.xValueAxis.valueMax = 5
l.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
l.xValueAxis.labelTextFormat = '%2.1f'
l.yValueAxis.valueMin = 0
l.yValueAxis.valueMax = 7
l.yValueAxis.valueSteps = [1, 2, 3, 5, 6]
d.add(l)
from reportlab.graphics import renderPDF
renderPDF.drawToFile(d, 'demo06.pdf')