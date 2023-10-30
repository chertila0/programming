#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] \
 + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
sofas_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] \
 + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1]['quantity'] \
 * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

lamps = store[goods['Лампа']][0]['quantity']
tables = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
sofas = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
chairs = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
print(f"Лампа - {lamps} шт, стоимость {lamps_cost} руб")
print(f"Стол - {tables} шт, стоимость {tables_cost} руб")
print(f"Диван - {sofas} шт, стоимость {sofas_cost} руб")
print(f"Стул - {chairs} шт, стоимость {chairs_cost} руб")

