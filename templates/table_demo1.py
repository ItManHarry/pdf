import os
os.chdir(r'd:\python\pdf')
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib.colors import green, red, blue, black, pink, grey, lavender, orange
from reportlab.lib.pagesizes import legal
from reportlab.lib.units import inch
tables = []
data = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
]
t = Table(data)
t.setStyle(TableStyle(
    [
        ('BACKGROUND', (1, 1), (-2, -2), green),
        ('TEXTCOLOR', (0, 0), (1, -1), red)
    ])
)
tables.append(t)
t2 = Table(data, 5*[0.4*inch], 4*[0.4*inch])
t2.setStyle(TableStyle([
    ('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
    ('TEXTCOLOR', (1, 1), (-2, -2), red),
    ('VALIGN', (0, 0), (0, -1), 'TOP'),
    ('TEXTCOLOR', (0, 0), (0, -1), blue),
    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
    ('TEXTCOLOR', (0, -1), (-1, -1), green),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
    ('BOX', (0, 0), (-1, -1), 0.25, black),
    ])
)
tables.append(t2)
t3 = Table(data, style=[
    ('GRID', (1, 1), (-2, -2), 1, green),
    ('BOX', (0, 0), (1, -1), 2, red),
    ('LINEABOVE', (1, 2), (-2, 2), 1, blue),
    ('LINEBEFORE', (2, 1), (2, -2), 1, pink),
])
tables.append(t3)
t4 = Table(data, style=[
    ('GRID', (0, 0), (-1, -1), 0.5, grey),
    ('GRID', (1, 1), (-2, -2), 1, green),
    ('BOX', (0, 0), (1, -1), 2, red),
    ('BOX', (0, 0), (-1, -1), 2, black),
    ('LINEABOVE', (1, 2), (-2, 2), 1, blue),
    ('LINEBEFORE', (2, 1), (2, -2), 1, pink),
    ('BACKGROUND', (0, 0), (0, 1), pink),
    ('BACKGROUND', (1, 1), (1, 2), lavender),
    ('BACKGROUND', (2, 2), (2, 3), orange),
])
tables.append(t4)
tables.append(Table(data))
doc = SimpleDocTemplate('table_demo1.pdf', pagesize=legal)
doc.build(tables)
