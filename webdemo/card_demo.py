import os
os.chdir(r'd:\python\pdf')
from reportlab.graphics.shapes import Drawing, Rect, String, Group, Line
from reportlab.lib import colors
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
def gen_card():
    d = Drawing()
    r = Rect(0, 0, 400, 200)
    r.fillColor = colors.beige
    d.add(r)
    wave = Group(
        Line(10, -5, 10, 10),
        Line(20, -15, 20, 20),
        Line(30, -5, 30, 10),
        Line(40, -15, 40, 20),
        Line(50, -5, 50, 10),
        Line(60, -15, 60, 20),
        Line(70, -5, 70, 10),
        Line(80, -15, 80, 20),
        Line(90, -5, 90, 10),
        String(15, -25, 'X&Y科技有限公司', fontName='STSong-Light', fontSize=6)
    )
    wave.translate(10, 170)
    d.add(wave)
    info = Group(
        String(0, 100, '程国前', textAnchor='middle', fontName='STSong-Light', fontSize=14, fillColor=colors.black),
        Line(-50, 85, 50, 85, strokeColor=colors.grey, strokeLineCap=1, strokeWidth=1),
        String(0, 60, '山东烟台开发区', textAnchor='middle', fontName='STSong-Light', fontSize=10, fillColor=colors.black),
    )
    info.translate(290, 10)
    d.add(info)
    contact = Group(
        String(0, 30, 'Tel:13780924007', fontName='STSong-Light', fontSize=8, fillColor=colors.black),
        String(0, 20, 'Email:jack_cheng@163.com', fontName='STSong-Light', fontSize=8, fillColor=colors.black),
        String(0, 10, 'Web:www.wave_audio.com', fontName='STSong-Light', fontSize=8, fillColor=colors.black),
    )
    contact.translate(20, 10)
    d.add(contact)
    return d
for i in range(10):
    renderPDF.drawToFile(gen_card(), 'card_damo'+str(i+1)+'.pdf')