import random
import matplotlib.pyplot as plt

def reload_function():
    XI = 0.0001
    YI = 0.0001
    while XI != round(XI,1) or XI != round(XI, 2) or XI != round(XI, 3) or YI != round(YI,1) or YI != round(YI, 2) or YI != round(YI, 3):

        m1 = 0.01
        while m1 != round(m1,1):
            XA = random.randint(-10,10)
            XB = random.randint(-10,10)
            YA = random.randint(-10,10)
            YB = random.randint(-10,10)

            A = (XA, YA) 
            B = (XB, YB) 

            if (XA != 0 and XB != 0 and YA != 0 and YB != 0 ) and (XB != XA and YB != YA):
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

            if (XC != 0 and XD != 0 and YC != 0 and YD != 0)  and (XD != XC and YD != YC):
                m2 = (D[1]- C[1]) / (D[0] - C[0])
            p2 = C[1] - (m2*C[0]) 

        if m1 != m2:
            nbx = m1 - m2
            nb = -p1 + p2
            XI = nb/nbx
            YI = m1*XI + p1

        
    print(XI, YI)

    return ([m1, round(p1,1), m2, round(p2,1), A, B, C, D, XI, YI])

# Obtain the values
valeur = reload_function()
resultat = f"Equation réduite de (AB) : {valeur[0]}x + {valeur[1]} \n Equation réduite de (CD) : {valeur[2]}x + {valeur[3]}"
print(resultat)

# Extract the values
m1, p1, m2, p2, A, B, C, D, XI, YI = valeur

# Create the plot
plt.figure(figsize=(10, 8))

# Plot the lines
x_values = range(-10, 11)
plt.plot(x_values, [m1*x + p1 for x in x_values], label=f'Line AB: {m1}x + {p1}')
plt.plot(x_values, [m2*x + p2 for x in x_values], label=f'Line CD: {m2}x + {p2}')

# Plot the points
plt.scatter([A[0], B[0], C[0], D[0], XI], [A[1], B[1], C[1], D[1], YI], color='red')
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')
plt.text(D[0], D[1], 'D', fontsize=12, ha='right')
plt.text(XI, YI, 'I', fontsize=12, ha='right', color='blue')

# Mark the intersection point
plt.scatter([XI], [YI], color='blue')

# Customize the plot
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Graphical Representation of Lines and Intersection Point')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Show the plot
plt.show()
