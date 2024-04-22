def result():
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