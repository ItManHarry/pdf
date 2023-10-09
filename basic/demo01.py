import os
from reportlab.pdfbase import pdfmetrics, ttfonts
os.chdir(r'D:\Python\pdf')
from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
from reportlab.lib.units import inch
# move the origin up and to the left
c.translate(inch, inch)
# define a large font
c.setFont("Helvetica", 80)
# choose some colors
c.setStrokeColorRGB(1, 0, 0)
c.setFillColorRGB(0.3, 0.1, 0.3)
# draw a rectangle
c.rect(inch, inch, 6*inch, 9*inch, fill=1)
# make text go straight up
c.rotate(90)
# change color
c.setFillColorRGB(0, 0, 1)
# say hello (note after rotate the y coord needs to be negative!)
# pdfmetrics.registerFont(ttfonts.TTFont('song', 'C:/Windows/Fonts/simfang.ttf'))  # 注册字体
c.drawString(inch, -3*inch, "Hello PDF File!")
c.showPage()
c.save()