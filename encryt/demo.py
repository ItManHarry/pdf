from reportlab.pdfgen import canvas
import os
from reportlab.lib import pdfencrypt
enc = pdfencrypt.StandardEncryption('rptlab', canCopy=0)
os.chdir(r'd:\python\pdf')
c = canvas.Canvas('encrypt.pdf', encrypt=enc)
c.drawString(100, 100, 'Hello world')
c.showPage()
c.save()