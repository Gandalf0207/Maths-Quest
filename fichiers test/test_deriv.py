import random
from math import *
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


while True:
    f_prime = 0.001
    while f_prime != round(f_prime,1) or f_prime != round(f_prime,2):
        num1 = random.randint(-20, 20)
        num2 = random.randint(-20, 20)
        num3 = random.randint(-20, 20)
        num4 = random.randint(-20, 20)
        num5 = random.randint(3, 5)
        num6 = random.randint(3, 10)

        num_resolve = random.randint(1,8)

        while num1 == 0 or num2 == 0 or num3==0 or num4 == 0:
            num1 = random.randint(-20, 20)
            num2 = random.randint(-20, 20)
            num3 = random.randint(-20, 20)
            num4 = random.randint(-20, 20)


        eqt = r"$f(x) = x^{%s} + \frac{%sx}{x} - %sx$"%(num5, num1, num6)
        f_prime = (num5*(num_resolve**(num5-1))) - ((num1*num_resolve)/(num_resolve**2)) - num6
    print(eqt)
    print(f"f'({num_resolve}) = {f_prime}")

    time.sleep(0.5)