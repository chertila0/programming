import random
def f(m, n):
    i = random.randint(m, n)
    while True:
        yield i
        i = random.randint(m, n)
a = input()
b = input()
g = f(a, b)

