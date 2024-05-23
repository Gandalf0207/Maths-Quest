import random
import time
def reload_function():

    XA = random.randint(-10,10)
    XB = random.randint(-10,10)
    XC = random.randint(-10,10)
    XD = random.randint(-10,10)

    YA = random.randint(-10,10)
    YB = random.randint(-10,10)
    YC = random.randint(-10,10)
    YD = random.randint(-10,10)

    m1 = 0.01
    while m1 != round(m1,1):
        XA = random.randint(-10,10)
        XB = random.randint(-10,10)
        YA = random.randint(-10,10)
        YB = random.randint(-10,10)

        A = (XA, YA) 
        B = (XB, YB) 

        if (XA != 0 and XB != 0 and XC != 0 and XD != 0 and YA != 0 and YB != 0 and YC != 0 and YD != 0) and (XB != XA and YB != YA):
            m1 = (B[1]- A[1]) / (B[0] - A[0])
        p1 = A[1] - (m1*A[0]) 


    m2 = 0.01
    while m2 != round(m2,1):

        XC = random.randint(-10,10)
        XD = random.randint(-10,10)
        YC = random.randint(-10,10)
        YD = random.randint(-10,10)

        C = (XC, YC)
        D = (XD, YD)

        if (XC != 0 and XD != 0 and XC != 0 and XD != 0 and YC != 0 and YD != 0 and YC != 0 and YD != 0) and (XD != XC and YD != YC):
            m2 = (D[1]- C[1]) / (D[0] - C[0])
        p2 = C[1] - (m2*C[0]) 



    return ([m1, p1, m2, p2, A, B, C, D])


while True:
    
    liste = reload_function()


    print("m1 = ", liste[0])
    print("p2 = ", liste[1])
    print("m2 = ", liste[2])
    print("p2 = ", liste[3])
    print("A = ", liste[4])
    print("B = ", liste[5])
    print("C = ", liste[6])
    print("D = ", liste[7])
    time.sleep(0.1)
