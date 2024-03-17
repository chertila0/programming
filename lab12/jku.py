from appJar import gui
from triangle import triangle as tri

app=gui()


app.setBg('light blue')
app.addLabel('Здравствуйте! Какую фигуру вы хотите выбрать?')
app.addLabelOptionBox('Figure',['Треугольник','Трапеция','Квадрат'])
app.addLabel('Отлично, теперь выберите что вы хотите посчитать:')
app.addLabelOptionBox('Параметр', ['Площадь фигуры','Радиус описанной окружности','Радиус вписанной окружности'])

def press(win):
    app.showSubWindow(win)

app.startSubWindow('Продолжить')

def result():
    app.infoBox('Результат вычислений', f'Результат равен {res}')

if app.getOptionBox('Figure') == 'Треугольник' and app.getOptionBox('Параметр') == 'Площадь фигуры':
    app.addNumericEntry('Сторона 1')
    app.addNumericEntry('Сторона 2')
    app.addNumericEntry('Сторона 3')
    app.addButton('Результат', result)
    res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).ploshad()


app.stopSubWindow()
app.addButton('Продолжить', press)

app.go()