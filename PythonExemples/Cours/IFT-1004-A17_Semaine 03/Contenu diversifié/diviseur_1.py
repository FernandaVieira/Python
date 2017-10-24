# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Fonction avec deux paramètres et retournant un booléen

def diviseur(a, b):
    return a % b == 0

print( diviseur(3, 15) ) # False
print( diviseur(15, 3) ) # True
print( diviseur(3 * 5, 2 + 1) ) # True 
print( diviseur(abs(-15), 4 - 1) ) # True
