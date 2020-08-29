from sympy import *
from sympy.plotting import (plot, plot_parametric,plot3d_parametric_surface, plot3d_parametric_line,plot3d)
x = symbols("x", real=True)
pf = ((x**3)-4*x+3)/((x-5)**2*(x**2+3)*(x**2+5))
pfdecomp = apart(pf)
print("a.)", pfdecomp)
a = symbols("a", positive=True)
pf2 = (x**2+2*x+a)/((x-1)**3*(x**2+1))
pf2decomp = apart(pf2, x)
print("b.) Function:", pf2)
print("b.) Decomposed:", pf2decomp)
pfdc1 = (a-3)/(4*(x-1))
pfdc2 = (a-1)/(2*(x-1)**2)
pfdc3 = (a+3)/(2*(x-1)**3)
pfdc4 = (a+3)/(4*(x**2+1))
pfdc5 = (x-1)/(4*x**2+1)
solve_a1 = integrate(pfdc1, (x, 2, 4))
print("Integral", solve_a1)
solve_a2 = integrate(pfdc2, (x, 2, 4))
solve_a3 = integrate(pfdc3, (x, 2, 4))
solve_a4 = integrate(pfdc4, (x, 2, 4))
solve_a5 = integrate(pfdc5, (x, 2, 4))
actual_a = solve((solve_a1-solve_a2+solve_a3-(solve_a4+solve_a5)), a)
print("Value of a", actual_a)
