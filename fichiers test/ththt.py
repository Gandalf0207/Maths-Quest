import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_system():
    # Génération de valeurs aléatoires pour les coefficients du système
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    # Création des équations du système
    eq1_constant = random.randint(1, 100)
    eq2_constant = random.randint(1, 100)
    
    # Affichage du système d'équations
    print("Système à résoudre:")
    print(f"{a}x + {b}y = {eq1_constant}")
    print(f"{c}x + {d}y = {eq2_constant}")
    print()
    
    # Résolution du système
    determinant = a*d - b*c
    if determinant == 0:
        return "Le déterminant est nul, le système n'a pas de solution unique."
    
    x_val_num, x_val_denom = d * eq1_constant - b * eq2_constant, determinant
    y_val_num, y_val_denom = a * eq2_constant - c * eq1_constant, determinant
    
    # Formatage des résultats en chaînes de caractères
    result_str = f"La valeur de x est {x_val_num}/{x_val_denom} et la valeur de y est {y_val_num}/{y_val_denom}"
    
    return result_str

# Exécution et affichage du résultat
print(solve_system())
