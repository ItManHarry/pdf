import os
from reportlab.pdfgen import canvas
os.chdir(r'D:\Python\pdf')
c = canvas.Canvas('demo4.pdf')
# c.setStrokeColorRGB(0, 0, 1)
pixels = c.drawInlineImage('hero.jpg', 0, 0, 500, 500)
print('Pixels : ', pixels)
c.setFillColorRGB(1, 0, 0)
# c.setFont('微软雅黑', 2)
c.drawString(0, 510, 'This is a picture of hero!')
c.showPage()
text = c.beginText(0, 550)
text.textLine('''
    This is a 
    test of text 
    drawing...
''')
c.drawText(text)
c.showPage()
c.save()