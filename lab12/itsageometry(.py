from appJar import gui
from rectangle import rectangle as rect
from trapezoid import trapezoid as trap
from triangle import triangle as tri

def press(btn):
    if btn == 'Выйти':
        app.stop()

app = gui()
app.addLabel('Здраствуйте! Пожалуйста, выберите фигуру:')
app.addButtons(['Треугольник', 'Квадрат','Трапеция'], press)
app.addEmptyLabel('')
app.addButton('Выйти', press)
app.go()