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

type_figure = ''
type_operation =''
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
def result(res):
    type_operation = app.getOptionBox('Параметр')
    type_figure = app.getOptionBox('Фигура')
    storona_1 = app.getEntry('Сторона 1')
    storona_2 = app.getEntry('Сторона 2')
    storona_3 = app.getEntry('Сторона 3')
    storona_4 = app.getEntry('Сторона 4')
    res = 'пусто'
    if type_operation == 'Площадь фигуры' and type_figure == 'Прямоугольник':
        if storona_1 != None and storona_2 != None and storona_3 == None and storona_4 == None:
            res = rect(storona_1, storona_2,storona_3,storona_4).ploshad()
        else: 
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Площадь фигуры' and type_figure == 'Треугольник':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 == None:
            res = tri(storona_1,storona_2,storona_3,storona_4).ploshad()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Площадь фигуры' and type_figure == 'Трапеция':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 != None:
            res = trap(storona_1,storona_2,storona_3,storona_4).ploshad()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Радиус описанной окружности' and type_figure == 'Прямоугольник':
        if storona_1 != None and storona_2 != None and storona_3 == None and storona_4 == None:
            res = rect(storona_1,storona_2,storona_3,storona_4).rad_opis()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Радиус описанной окружности' and type_figure == 'Треугольник':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 == None:
            res = tri(storona_1,storona_2,storona_3,storona_4).rad_opis()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Радиус описанной окружности' and type_figure == 'Трапеция':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 != None:
            res = trap(storona_1, storona_2, storona_3,storona_4).rad_opis()
    if type_operation == 'Радиус вписанной окружности' and type_figure == 'Прямоугольник':
        if storona_1 != None and storona_2 != None and storona_3 == None and storona_4 == None:
            res = rect(storona_1,storona_2,storona_3,storona_4).rad_vpis()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Радиус вписанной окружности' and type_figure == 'Треугольник':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 == None:
            res = tri(storona_1,storona_2,storona_3,storona_4).rad_vpis()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    if type_operation == 'Радиус вписанной окружности' and type_figure == 'Трапеция':
        if storona_1 != None and storona_2 != None and storona_3 != None and storona_4 != None:
            res = trap(storona_1,storona_2,storona_3,storona_4).rad_vpis()
        else:
            res = "Вы ошиблись при вводе сторон! Подсказка: вводите стороны по порядку"
    app.infoBox('',f'Результат: {res}')

app.addButton('Рассчитать', result)
app.stopSubWindow()
app.addButton('Продолжить',press)
app.go()