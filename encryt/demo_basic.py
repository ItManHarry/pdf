import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
title = "Hello world"
pageinfo = "platypus example"
PAGE_HEIGHT = 14*inch
PAGE_WIDTH = 10*inch
styles = getSampleStyleSheet()
def firstPage(c, doc):
    c.saveState()
    c.setFont('Times-Bold', 16)
    c.drawCentredString(PAGE_WIDTH / 3.0, 10*inch, title)
    c.setFont('Times-Roman', 9)
    c.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    c.restoreState()
def laterPages(c, doc):
    c.saveState()
    c.setFont('Times-Roman', 9)
    c.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    c.restoreState()
def go():
    doc = SimpleDocTemplate("platypus_demo1.pdf")
    story = [Spacer(1, 2*inch)]
    style = styles["Normal"]
    for i in range(100):
        bogus_text = ("This is Paragraph number %s. " % i) * 20
        p = Paragraph(bogus_text, style)
        story.append(p)
        story.append(Spacer(1, 0.2*inch))
    doc.build(story, onFirstPage=firstPage, onLaterPages=laterPages)
    # doc.build(story)
go()