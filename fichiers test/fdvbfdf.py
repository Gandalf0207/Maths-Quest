import random

def reload_function():
    def equation_reduite(droite1, droiteB):
        m1 = (droite1[1][1] - droite1[0][1]) / (droite1[1][0] - droite1[0][0])
        print(m1)

        while m1 != round(m1,1):
            reload_function()

        # (yB - yA)/(xB-xA)






    
    XA = random.randint(-10,10)
    XB = random.randint(-10,10)
    XC = random.randint(-10,10)
    XD = random.randint(-10,10)

    YA = random.randint(-10,10)
    YB = random.randint(-10,10)
    YC = random.randint(-10,10)
    YD = random.randint(-10,10)

    while XA == YA or XB == YB or XC == YC or XD == YD or 0 in Check_division:
        YA = random.randint(-10,10)
        YB = random.randint(-10,10)
        YC = random.randint(-10,10)
        YD = random.randint(-10,10)

    A = (XA, YA) 
    B = (XB, YB) 
    C = (XC, YC)
    D = (XD, YD)
    print("A = ", A)
    print("B = ", B)
    print("C = ", C)
    print("D = ", D)

    return ([equation_reduite((A, B), (C, D)), A, B, C, D])


reload_function()