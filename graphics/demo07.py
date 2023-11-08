import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib import colors
d = Drawing()
p = Pie()
p.x = 65
p.y = 50
p.width = 70
p.height = 70
p.data = [10, 20, 30, 40, 50, 60]
p.labels = ['a', 'b', 'c', 'd', 'e', 'f']
p.slices.strokeWidth = 0.5
p.slices[2].fillColor = colors.yellow
p.slices[3].popout = 10
p.slices[3].strokeWidth = 2
p.slices[3].strokeDashArray = [2, 2]
p.slices[3].labelRadius = 1.75
p.slices[3].fontColor = colors.red
d.add(p)
renderPDF.drawToFile(d, 'demo07.pdf')
renderSVG.drawToFile(d, 'demo07.svg')