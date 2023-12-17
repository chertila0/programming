from functools import wraps



def f(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

# def hg(n):
#     def gh(m):
#         return n*m
#     return gh
# @f(4)
# def g(x,y):
#     return hg(x)(y)
# print(g(5,6))
@f(4)
# def calc(x,y,z):
#     return make_calc(x,y)(z)
# print(calc('+', 1, 3))
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

print(make_calc('+',1)(2))


