# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Exemple avec l'approche TDD (Test Driven Development)

def minimum(a, b, c):
    if a <= b and a <= c:
        return a

    if b <= a and b <= c:
        return b

    if c <= a and c <= b:
        return c

def maximum(a, b, c):
    if a >= b and a >= c:
        return a

    if b >= a and b >= c:
        return b

    if c >= a and c >= b:
        return c

def somme(a, b, c):
    return a + b + c

def mediane(a, b, c):
    if a == b == c:
        return a
        
    return somme(a, b, c) - minimum(a, b, c) - maximum(a, b, c) 

assert mediane(5, 6, 2) == 5
assert mediane(1, 1, 1) == 1
assert mediane(-2, -5, -1) == -2
