import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis, XValueAxis
d = Drawing()
data = [(10, 20, 30, 40), (15, 22, 37, 42)]
x = XCategoryAxis()
x.setPosition(75, 50, 300)
x.configure(data)
x.categoryNames = ['Beer', 'Wine', 'Meat', 'Cannelloni']
x.labels.boxAnchor = 'n'
x.labels[3].dy = -15
x.labels[3].angle = 30
x.labels[3].fontName = 'Times-Bold'
y = YValueAxis()
y.setPosition(50, 50, 125)
y.configure(data)
d.add(x)
d.add(y)
x_data = [(0, 10, 20, 30, 40)]
y_data = [(0, 50, 100, 150, 200)]
x_axes = XValueAxis()
x_axes.setPosition(80, 80, 100)
x_axes.configure(x_data)
x_axes.labels.boxAnchor = 'n'
y_axes = YValueAxis()
y_axes.setPosition(80, 80, 100)
y_axes.configure(y_data)
d.add(x_axes)
d.add(y_axes)
from reportlab.graphics import renderPDF
renderPDF.drawToFile(d, 'demo3.pdf')