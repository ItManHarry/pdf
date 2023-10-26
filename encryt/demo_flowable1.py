from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import os
os.chdir(r'd:\python\pdf')
stylesheet = getSampleStyleSheet()
style = stylesheet['BodyText']
p = Paragraph('This is a very silly example', style)
c = canvas.Canvas('demo_flowable1.pdf')
available_width = 460
available_height = 800
width, height = p.wrap(available_width, available_height)
print(f'Available Width {available_width} , height {available_height}')
print(f'Wrapped width {width}, height {height}')
if width <= available_width and height <= available_height:
    p.drawOn(c, 0, available_height)
    available_height = available_height - height
    print(f'Available Width {available_width} , height {available_height}')
    print(f'Wrapped width {width}, height {height}')
    c.save()
else:
    raise ValueError('Not enough room')