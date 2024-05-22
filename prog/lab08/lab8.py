from functools import wraps



def f(n):
    def decorator(func):
        results = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            if not(args or kwargs):
                return results
            else:
                for _ in range(n):
                    result = func(*args, **kwargs)
                    results.append(result)
                return result
        return wrapper
    return decorator


def make_calc(operation, a):
    @f(4)
    def cilc(b=1):
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


