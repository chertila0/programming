def make_calc(operation, a):
    
    def cilc(b):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return round(a / b, 2)
    return cilc
calc = make_calc('+', a=1)
print(calc(5))