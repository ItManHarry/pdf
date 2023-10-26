import os
from reportlab.pdfgen import  canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
os.chdir(r'd:\python\pdf')
styles = getSampleStyleSheet()
style_normal = styles['Normal']
style_head = styles['Heading1']
story = []
story.append(Paragraph('This is a Heading', style_head))
story.append(Paragraph('This is a Paragraph in <i>Normal</i>', style_normal))
c = canvas.Canvas('demo_flowable2.pdf')
f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1)
f.addFromList(story, c)
c.save()