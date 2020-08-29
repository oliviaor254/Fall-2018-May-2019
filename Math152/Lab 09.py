from sympy import *
from sympy.plotting import (plot)
x, n = symbols('x n')
An = (((-1)**n)*(n+1)*(2**n)*((x-2)**n))/(9**(n+2))
An_1 = (((-1)**(n+1))*(n+2)*((2)**(n+1))*((x-2)**(n+1)))/(9**(n+3))
An_simpl = abs(simplify(An_1/An))


# Radius of Convergence = 1/2; [5/2,13/2) (Double Check) (ABS should be 2(x-2)/Attempt by hand)
AnLim = Limit(An_simpl, n, oo).doit()
print("Limit going to inf:", AnLim)

lowerlim = ((-1**n)*(n+1)*(2**n)*((5/2)-2)**n)/(9**(n+2))
lowerlim1 = (-1**(n+1)*(n+2)*(2**(n+1))*((5/2)-2)**(n+1))/(9**(n+3))

print("Limit at x=5/2: ", limit(abs(simplify(lowerlim1/lowerlim)), n, oo))
upperlim = ((-1**n)*(n+1)*(2**n)*((13/2)-2)**n)/(9**(n+2))
upperlim1 = (-1**(n+1)*(n+2)*(2**(n+1))*((13/2)-2)**(n+1))/(9**(n+3))
bn1 = ((n+2)*(2**(n+1))*((13/2)-2)**(n+1))/(9**(n+3))
print("Limit at x=13/2: Indeterminante. Use alt. series Test:", limit(abs(simplify(upperlim1/upperlim)), n, oo))
print("bn =", bn1)
bn = Limit(abs(((n+2)*(2**(n+1))*((13/2)-2)**(n+1))/(9**(n+3))), n, oo).doit()
print("Limit as bn goes n to infinity", bn, "Therefore the interval is (5/2,13/2]")
fx = 1/((5+2*x)**2)
s5 = Sum(An, (n, 0, 5)).doit()
s10 = Sum(An, (n, 0, 10)).doit()
s15 = Sum(An, (n, 0, 15)).doit()
plot(s5, s10, s15, fx, xlim=[-4, 9], ylim=[-4, 4])
