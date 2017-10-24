# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Exemple de module

"""
Module permettant d'effectuer les 4
opérations arithmétiques de base.
"""

def addition(a, b):
    """Fonction permettant de faire l'addition
    de deux nombres passés comme arguments.

    Args:
        a (int): Premier nombre
        b (int): Second nombre
    
    Returns:
        sum (int): Somme de a et b
    """
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    # TODO: Gérer le cas ou b == 0
    return a / b

print(__name__)

if __name__ == '__main__':
    assert addition(2, 5) == 7
    assert addition(4, 0) == 4
    assert addition(4, 8) == 13
