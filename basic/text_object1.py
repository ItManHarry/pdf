import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
os.chdir(r'd:\python\pdf')
def cursormove(cv):
    text_object = cv.beginText()
    text_object.setTextOrigin(inch, 3*inch)
    x, y = text_object.getCursor()
    print(f'x is {x}, y is {y}')
    text_object.setFont('Helvetica-Oblique', 14)
    for line in range(8):
        text_object.textLine(f'This is text line {line}!')
    text_object.setFillGray(0.4)
    text_object.textLines('''
        With many apologies to the Beach Boys
        and more else who finds this objectionable
    ''')
    cv.drawText(text_object)
    x, y = text_object.getCursor()
    print(f'x is {x}, y is {y}')
cv = canvas.Canvas('text_object1.pdf')
cursormove(cv)
cv.showPage()
cv.save()