from sympy import symbols, diff, sin, cos 
 
x, y = symbols("x y") 
f = x/(x + y)
 
df_dx = diff(f, x) # частная производная по x 
df_dy = diff(f, y) # частная производная по y

df_dxdx = diff(df_dx, x) # смешанная производная по х
df_dxdy = diff(df_dx, y) # смешанная производная по х и у
df_dydy = diff(df_dy, y) # смешанная производная по у
 
args = [(x, 1), (y, 1)] # аргументы для подстановки, x = 1, y = 1 
 
df = df_dx.subs(args)*x + df_dy.subs(args)*y # первый дифференциал 
df2 = -(1/2)*(df_dxdx.subs(args)*(x - 1)*(x - 1) + 2*df_dxdy.subs(args)*(x - 1)*(y - 1) + df_dydy.subs(args)*(y - 1)*(y - 1))
Taylor_polynomial = f.subs(args) + df + df2 # многочлен Тейлора 2-й степени 
 
print("P(x, y) = ", Taylor_polynomial)