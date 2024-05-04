import random
from sympy import symbols, Eq, solve
from fractions import Fraction

def solve_system():
    # Génération de valeurs aléatoires pour les coefficients du système
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    # Création des symboles pour les inconnues
    x, y = symbols('x y')
    
    # Création des équations du système
    eq1 = Eq(a*x + b*y, random.randint(1, 100))
    eq2 = Eq(c*x + d*y, random.randint(1, 100))
    
    # Résolution du système
    solution = solve((eq1, eq2), (x, y))
    
    # Extraction des valeurs exactes sous forme de fractions
    x_val = solution[x]
    y_val = solution[y]
    
    # Formatage des résultats en chaînes de caractères
    result_str = "La valeur de x est {} et la valeur de y est {}".format(Fraction(x_val).limit_denominator(), Fraction(y_val).limit_denominator())
    
    return result_str

# Exécution et affichage du résultat
print(solve_system())
