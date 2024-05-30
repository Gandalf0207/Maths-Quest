import random

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def segments_intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# Exemple d'utilisation
xA = random.randint(-10,10)
xB = random.randint(-10,10)
yA = random.randint(-10,10) 
yB = random.randint(-10,10)
xC = random.randint(-10,10)
xD = random.randint(-10,10)
yC = random.randint(-10,10) 
yD = random.randint(-10,10) 








A = (xA, yA)
B = (xB, yB)
C = (xC, yC)
D = (xD, yD)

if segments_intersect(A, B, C, D):
    print("Les segments s'intersectent.")
else:
    print("Les segments ne s'intersectent pas.")
