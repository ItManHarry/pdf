import os
from reportlab.lib.units import cm
from reportlab.lib.colors import Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import legal
from reportlab.platypus import Paragraph, SimpleDocTemplate
os.chdir(r'd:\python\pdf')
style = ParagraphStyle(
    name='Test',
    alignment=0,
    allowOrphans=0,
    allowWidows=1,
    backColor='#FFFF00',
    borderColor='#000000',
    borderPadding=(7, 2, 20),
    borderWidth=1,
    bulletAnchor='start',
    bulletFontName='Helvetica',
    bulletFontSize=10,
    bulletIndent=0,
    embeddedHyphenation=1,
    endDots=None,
    firstLineIndent=0,
    fontName='Helvetica',
    fontSize=10,
    hyphenationLang='en_GB',
    justifyBreaks=0,
    justifyLastLine=0,
    leading=12,
    leftIndent=0,
    linkUnderline=0,
    rightIndent=0,
    spaceAfter=0,
    spaceBefore=0,
    spaceShrinkage=0.05,
    splitLongWords=1,
    strikeColor=None,
    strikeGap=1,
    strikeOffset=0.25*cm,
    strikeWidth=None,
    textColor=Color(0, 0, 0, 1),
    textTransform=None,
    underlineColor=None,
    underlineGap=1,
    underlineOffset=-0.125*cm,
    underlineWidth=None,
    uriWasteReduce=0.3,
    wordWrap=None,
)
paragraphs = []
text = '''
    You are hereby charged that on the
    28th day of May, 1970, you did willfully,
    unlawfully, and with malice of forethought,
    publish an alleged English-
    Hungarian phrase book with intent
    to cause a breach of the peace. How do
    you plead?
'''
paragraphs.append(Paragraph(text, style=style))
doc = SimpleDocTemplate('paragraph_demo1.pdf', pagesize=legal)
doc.build(paragraphs)