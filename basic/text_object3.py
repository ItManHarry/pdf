import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('text_object3.pdf')
def char_space(cv):
    text_object = cv.beginText()
    text_object.setTextOrigin(3, 5.5*inch)
    text_object.setFont('Helvetica', 10)
    space = 0
    for line in range(8):
        text_object.setCharSpace(space)
        text_object.textLine(f'char space is {space}, line number is {line+1}')
        space += 0.5
    text_object.setFillGray(0.4)
    text_object.textLines('''
        With many apologies to the Beach Boys
        and anyone else who finds this objectionable
    ''')
    cv.drawText(text_object)
char_space(cv)
cv.line(0, 3.5*inch, 3*inch, 3.5*inch)
cv.showPage()
cv.save()