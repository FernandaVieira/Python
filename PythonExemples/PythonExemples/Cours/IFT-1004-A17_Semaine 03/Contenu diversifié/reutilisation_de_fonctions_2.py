# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Réutilisation de fonctions

def diviseur(a, b):
    return a % b == 0

def pair(n):
    return diviseur(n, 2)

def impair(n):
    return not pair(n)

print( impair(2) )  # False
print( impair(5) )  # True
print( impair(7) )  # True
print( impair(15) ) # True
print( impair(10) ) # False

x = 21
if impair(x):
    print('{} est impair.'.format(x))
else:
    print("{} n'est pas impair.".format(x))
