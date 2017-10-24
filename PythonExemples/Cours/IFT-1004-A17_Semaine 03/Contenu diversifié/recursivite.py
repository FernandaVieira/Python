# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Réutilisation de fonctions

def diviseur(a, b):
    return a % b == 0

def pair(n):
    return not impair(n)

def impair(n):
    return not pair(n)

print( impair(2) ) # Maximum recursion depth exceeded
