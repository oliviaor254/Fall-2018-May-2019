from sympy import *  ##NEED TO RUN AND TEST ALL CODE
import matplotlib.pyplot as plt
from sympy.plotting import (plot, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line, plot3d)

n, x, t = symbols('n x t', real=true)
powerS = x ** (8 * n + 2) / (8 * n + 2)
powerS_1 = x ** (8 * (n + 1) + 2) / (8 * (n + 1) + 2)
intofcon = simplify(powerS_1 / powerS)
print(limit(intofcon, n, oo))
# Radius of convergence is from -1 to 1
tfun = t / (1 - t ** 8)
fx = integrate(tfun, (t, 0, x))
print(fx)
ans = -log((-1) ** 2 - 1) / 8 + log((-1) ** 2 + 1) / 8 + atan(-1 ** 2) / 4
print(ans)
s1 = Sum(powerS, (n, 1, 1)).doit()
s3 = Sum(powerS, (n, 1, 3)).doit()
s5 = Sum(powerS, (n, 1, 5)).doit()
##PLOT POLYNOMIALS
plot(s5, s3, s1, (x, -1.5, 1.5), (0, 2))
#NEED TO WORK ON PLOTTING GRAPH

#Endpoints is where you plug in number for that x and plg
