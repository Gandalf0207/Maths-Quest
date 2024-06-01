import random
from math import *



x1 =0.001
x2 = 0.001

while x1 != round(x1,1) or x1 != round(x1, 2) or x2 != round(x2,1) or x2 != round(x2, 2):

    nb1 = random.randint(-7,7)
    nb2 = random.randint(2,25)
    nb3 = random.randint(2,10)

    while nb1 ==0 or nb1 ==-1 or nb1==1:
        nb1 = random.randint(-15,15)

    eqt = r"$ (%sx)^2 + %sx + %s$"%(nb1, nb2, nb3)

    delta = nb2**2 - (4*nb1*nb3)

    if delta > 0:
        x1 = (-nb2 - sqrt(delta)) / (2*nb1)
        x2 = (-nb2 + sqrt(delta)) / (2*nb1)



resultat = f"x1 = {x1} \nx2 = {x2}"
resultat2 = f"x1 = {x2} \nx2 = {x1}"
resultat3 = f"x1 = {x1+1} \nx2 = {x2}"

print(eqt , resultat)
