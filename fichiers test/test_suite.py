import random

U0 = random.randint(-10,10)
r = random.randint(-10,10)
n = random.randint(2,15)

while U0 == 0:
    U0 = random.randint(-10,10)

if random.randint(0,1) == 0 :
    U1 = U0 + r
    U2 = U1 + r
    eqt = f"U0 = {U0}\nU1 = {U1}\nU2 = {U2}"
    print("trouver la raison de cette suite et calculer la somme des",n,"premiers termes")
    somme_suite = (n/2)*(2*U0+(n-1)*r)
else :
    U1 = U0*r
    U2 = U0*(r**2)
    eqt = f"U0 = {U0}\nU1 = {U1}\nU2 = {U2}"
    print("trouver la raison de cette suite et calculer la somme des",n,"premiers termes")
    somme_suite = U0*((1-(r**n))/(1-r))


print(eqt)
print(somme_suite)