import random
#Script provenat de stack overflow et adapté par nous
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return int(x), int(y)

XA = random.randint(-50,50)
XB = random.randint(-50,50)
XC = random.randint(-50,50)
XD = random.randint(-50,50)

YA = random.randint(-50,50)
YB = random.randint(-50,50)
YC = random.randint(-50,50)
YD = random.randint(-50,50)
while XA == YA or XB == YB or XC == YC or XD == YD:
    YA = random.randint(-50,50)
    YB = random.randint(-50,50)
    YC = random.randint(-50,50)
    YD = random.randint(-50,50)

A = (XA, YA) 
B = (XB, YB) 
C = (XC, YC)
D = (XD, YD)
print (line_intersection((A, B), (C, D)))
print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)