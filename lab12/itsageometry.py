from appJar import gui
from triangle import triangle as tri
from rectangle import rectangle as rect
from trapezoid import trapezoid as trap

app=gui()


app.setBg('light blue')
app.addLabel('Здравствуйте! Какую фигуру вы хотите выбрать?')
app.addLabelOptionBox('Фигура',['Треугольник','Трапеция','Прямоугольник'])
app.addLabel('Отлично, теперь выберите что вы хотите посчитать:')
app.addLabelOptionBox('Параметр', ['Площадь фигуры','Радиус описанной окружности','Радиус вписанной окружности'])


def press(win):
    app.showSubWindow(win)

        

app.startSubWindow('Продолжить')
app.addLabel('Введите стороны выбранной фигуры.')
app.addLabel('Подсказка: для прямоугольника достаточно 2-х строн, для треугольника необходимо ввести все 3 стороны,')
app.addLabel(' для трапеции необходимо ввести все 4 стороны.')
app.addLabel('Заполните столько полей ввода, сколько вам необходмо. Оставшиеся оставьте пустыми')
app.addNumericEntry('Сторона 1')
app.addNumericEntry('Сторона 2')
app.addNumericEntry('Сторона 3')
app.addNumericEntry('Сторона 4')

app.startSubWindow("Рассчитать")
app.addLabel('Я молодец')
app.stopSubWindow()

app.addButton('Рассчитать', press)
app.stopSubWindow()
app.addButton('Продолжить',press)
app.go()