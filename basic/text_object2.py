import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
def cursor_move(cv):
    text_object = cv.beginText()
    text_object.setTextOrigin(2, 2.5*inch)
    text_object.setFont('Helvetica', 14)
    for line in range(8):
        text_object.textOut(f'This is text line , line number is {line+1}')
        text_object.moveCursor(14, 14)
    text_object.setFillColorRGB(0.4, 0, 1)
    text_object.textLines('''
        With many apologies to the Beach Boys
        and anyone else who finds this objectionable
    ''')
    cv.drawText(text_object)
os.chdir(r'd:\python\pdf')
cv = canvas.Canvas('text_object2.pdf')
cursor_move(cv)
cv.showPage()
cv.save()