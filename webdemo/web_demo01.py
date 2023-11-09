import os
os.chdir(r'd:\python\pdf')
from reportlab.pdfgen import canvas
c = canvas.Canvas('web_demo01.pdf', pagesize=(595.27, 841.89))
c.drawString(50, 780, 'Hello ReportLab Again!')
c.showPage()
c.save()