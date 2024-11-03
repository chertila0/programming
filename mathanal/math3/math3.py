import sympy
from sympy.abc import x
from sympy import sin

f = (1 + sin(x))**2
print(f.integrate(x))