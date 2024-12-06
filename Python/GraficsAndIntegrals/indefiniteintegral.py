from sympy import Symbol, integrate, sin, plot
x = Symbol('x')
print(integrate(sin(x), x))
expr1=1 / (x**2 + 1)
expr2=1 / (x**2 + 2)
expr3=1 / (x**2 + 3)
expr4=1 / (x**2 + 4)
expr5=1 / (x**2 + 5)
plot(expr1, expr2, expr3, expr4, expr5, (x, -0.5, 5.5))
