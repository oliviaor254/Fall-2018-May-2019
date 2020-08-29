from sympy import *    ##NEED TO RUN AND TEST ALL CODE
from numpy import *
#import matplotlib.pyplot as plt
from sympy.plotting import (plot, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line, plot3d)
x, n = symbols('x n', real=true)
An = n/(n**4+1)
gx = 1/(x**3)
fx = x/(x**4+1)
##GRAPH
p2 = plot(fx,gx, (x, 1, 20),line_color='g')
print("Integration", integrate(fx))
print("Integration to infinity", integrate(fx, (x, 1, oo)))
s10 = [An for n in range(1, 10)]
s10sum = cumsum(s10)
print(s10sum)
s50 = [An for n in range(1, 50)]
s50sum = cumsum(s50)
s100 = [An for n in range(1, 100)]
s100sum = cumsum(s100)
overallSum = Sum(An, (n, 1, oo)).doit()   #Unsure if correct method

print("Remainder Estimate")     #Unsure of how to do/start
print("Actual remainder")   #<----- HAVE TO USE REMAINDER TEST
st = overallSum-s100sum    #BUGGY
print(float(st))

