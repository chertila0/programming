from appJar import gui
from triangle import triangle as tri

app=gui()


app.setBg('light blue')
app.addLabel('Здравствуйте! Какую фигуру вы хотите выбрать?')
app.addLabelOptionBox('Фигура',['Треугольник','Трапеция','Квадрат'])
app.addLabel('Отлично, теперь выберите что вы хотите посчитать:')
app.addLabelOptionBox('Параметр', ['Площадь фигуры','Радиус описанной окружности','Радиус вписанной окружности'])

def press(win):
    app.showSubWindow(win)

        

app.startSubWindow('Продолжить')
app.addNumericEntry('Сторона 1')
app.addNumericEntry('Сторона 2')
app.addNumericEntry('Сторона 3')
app.addNumericEntry('Сторона 4')
def result(res):
    if app.getEntry('Сторона 3') == None and app.getEntry('Сторона 4') == None:
        pass
    elif app.getEntry('Сторона 4') == None:
        if app.getOptionBox('Параметр') == 'Площадь фигуры':
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).ploshad()
        elif app.getOptionBox('Параметр') == 'Радиус описанной окружности':
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).rad_opis()
        else:
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).rad_vpis()
        app.infoBox('', f'Результат:{res}')
app.addButton('Рассчитать', result)
app.stopSubWindow()
app.addButton('Продолжить', press)

app.go()