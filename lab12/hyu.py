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
app.addLabel('Заполните столько полей ввода, сколько вам необходмо. Оставшиеся поля оставьте пустыми.')
app.addNumericEntry('Сторона 1')
app.addNumericEntry('Сторона 2')
app.addNumericEntry('Сторона 3')
app.addNumericEntry('Сторона 4')
def result(res):
    if app.getEntry('Сторона 1') == None or app.getEntry('Сторона 2') == None or app.getEntry('Сторона 3') == None and app.getEntry('Сторона 4') != None:
        res = 'Кажется вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку, не пропуская поля ввода.'
    elif app.getEntry('Сторона 3') == None and app.getEntry('Сторона 4') == None:
        if app.getOptionBox('Параметр') == 'Площадь фигуры':
            res = rect(app.getEntry('Сторона 1'), app.getEntry('Сторона 2')).ploshad()
        elif app.getOptionBox('Параметр') == 'Радиус описанной окружности':
            res = rect(app.getEntry('Сторона 1'), app.getEntry('Сторона 2')).rad_opis()
        else:
            res = rect(app.getEntry('Сторона 1'), app.getEntry('Сторона 2')).rad_vpis()
    elif app.getEntry('Сторона 4') == None:
        if app.getOptionBox('Параметр') == 'Площадь фигуры':
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).ploshad()
        elif app.getOptionBox('Параметр') == 'Радиус описанной окружности':
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).rad_opis()
        else:
            res = tri(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3')).rad_vpis()
    else:
        if app.getOptionBox('Параметр') == 'Площадь фигуры':
            res = trap(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3'), app.getEntry('Сторона 4')).ploshad()
        elif app.getOptionBox('Параметр') == 'Радиус описанной окружности':
            res = trap(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3'), app.getEntry('Сторона 4')).rad_opis()
        else:
            res = trap(app.getEntry('Сторона 1'), app.getEntry('Сторона 2'), app.getEntry('Сторона 3'), app.getEntry('Сторона 4')).rad_vpis()
    app.infoBox('', f'Результат:{res}')
app.addButton('Рассчитать', result)
app.stopSubWindow()
app.addButton('Продолжить', press)

app.go()