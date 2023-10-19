import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
os.chdir(r'd:\python\pdf')
c = canvas.Canvas('asian_demo.pdf')
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
c.setFont('STSong-Light', 16)
msg = u'简体中文'
print(msg)
c.drawString(100, 675, msg)
c.showPage()
c.save()