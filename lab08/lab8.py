from functools import wraps



def f(n):
    def decorator(func):
        results = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results if 
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
            a = round(a / b, 2)
        return a
    return cilc

print(make_calc('+', 1)(1))
