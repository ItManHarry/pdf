import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
os.chdir(r'd:\python\pdf')
styles = getSampleStyleSheet()
style_normal = styles['Normal']
style_head = styles['Heading1']
story = []
story.append(Paragraph('This is a Heading', style_head))
story.append(Paragraph('This is a Paragraph in <i>Normal</i>', style_normal))
doc = SimpleDocTemplate('demo_flowable3.pdf', pagesize=letter)
doc.build(story)