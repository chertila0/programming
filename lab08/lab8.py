def make_calc(operation, a):
    def cilc(b):
        nonlocal a
        if operation == '+':
            a += b
        elif operation == '-':
            a -= b
        elif operation == '*':
            a *= b
        elif operation == '/':
            a =  round(a / b, 2)
        return a
    return cilc
calc = make_calc('+', a=1)
print(calc(5))
print(calc(7))
