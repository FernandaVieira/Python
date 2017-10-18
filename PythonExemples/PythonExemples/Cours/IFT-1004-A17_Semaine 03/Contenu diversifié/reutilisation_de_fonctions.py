# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Réutilisation de fonctions

def diviseur(a, b):
    return a % b == 0

def pair(n):
    return diviseur(n, 2)

print( pair(2) )  # True
print( pair(5) )  # False
print( pair(7) )  # False
print( pair(15) ) # False
print( pair(10) ) # True

x = 21
if pair(x):
    print('{} est pair.'.format(x))
else:
    print("{} n'est pas pair.".format(x))
