import random
from math import *
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
c = 0
k = int(input("blablabla : "))
for i in range(k):


    choix_derive = random.randint(1,2)
    f_prime = 0.001
    c+=1
    while f_prime != round(f_prime,1) and f_prime != round(f_prime,2):
        num_resolve = random.randint(1,8)
        num1 = random.randint(-3, 3)
        num2 = random.randint(-20, 20)
        num3 = random.randint(-20, 20)
        num4 = random.randint(2, 4)
        num5 = random.randint(3, 5)
        num6 = random.randint(3, 10)


        while num1 == 0 or num2 == 0 or num3==0 or num4 == 0:
            num1 = random.randint(-3,3)
            num2 = random.randint(-20, 20)
            num3 = random.randint(-20, 20)
            num4 = random.randint(2, 4)

        if (choix_derive == 1):

            eqt = r"$f(x) = x^{%s} + \frac{x^%s}{%sx} - %sx$"%(num5, num1, num4, num6)
            deriv1 = num5 * (num_resolve**(num5-1))
            u = num_resolve**num1
            u_prime = num1*(num_resolve**(num1-1))
            v = num4*num_resolve
            v_prime = num4

            deriv2 = ((u_prime*v) - (u*v_prime))/v**2
            deriv3 = num6
            f_prime = deriv1 + deriv2 - deriv3
    
        else:

            eqt = r"$f(x) = \sqrt{x} + %sx - %sx^{%s}$"%( num5, num4, num1)

            deriv1 = (1) / (2*(sqrt(num_resolve)))
            deriv2 = num5
            deriv3 = num4*(num1*(num_resolve**(num1-1)))

            f_prime = deriv1 + deriv2 - deriv3


    print(eqt)
    print(deriv1)
    print(f"f'({num_resolve}) = {f_prime}")
    print(c)

