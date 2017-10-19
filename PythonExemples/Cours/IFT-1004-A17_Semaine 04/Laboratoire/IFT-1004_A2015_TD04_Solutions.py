__author__ = 'Jean-Francis Roy'
import math


def diviseur(a, b):
    """Détermine si l'entier b est un diviseur de l'entier a.

    Args:
        a (int): l'entier duquel diviser la valeur b
        b (int): le potentiel diviseur de a

    Returns:
        bool: True si b est un diviseur de a, False autrement.
    """

    return a % b == 0


def premier(n):
    """Détermine si un nombre n est premier.

    Args:
        n (int): le nombre dont nous voulons vérifier s'il est premier ou non

    Returns:
        bool: True si n est premier, False autrement
    """
    # Gestion des cas limite: aucun nombre plus petit que 2 est premier.
    if n < 2:
        return False

    # Autre cas limite: notre code ci-bas ne gère pas le cas où n = 2, alors nous le
    # gérons individuellement.
    elif n == 2:
        return True

    # Devons nous itérer jusqu'à n-1? Aller jusqu'à la racine carrée de n est suffisant!
    racine = math.ceil(math.sqrt(n))
    for i in range(2, racine + 1):
        if diviseur(n, i):
            return False  # On retourne directement False ici : on a trouvé notre contre-exemple.
                          # Cette solution est alternative à celle présentée en classe.

    return True


def trouver_deux_facteurs_premiers(n):
    """Trouve et affiche à l'écran les deux facteurs premiers d'un nombre n, si possible.

    Args:
        n (int): le nombre à factoriser
    """

    # On parcoure les nombres entre 2 et n//2.
    i = 2
    trouve = False
    racine = math.ceil(math.sqrt(n))
    while i <= racine and not trouve:
        # Si i est un diviseur (facteur) de n, on vérifie s'il est premier. Si c'est le cas, on vérifie si
        # le second facteur est également premier. Si oui, on a gagné!
        if diviseur(n, i) and premier(i):
            if premier(n // i):
                print("Les deux facteurs premiers de {} sont {} et {}!".format(n, i, n//i))
                trouve = True
            else:
                # Optimisation: Si i est un diviseur premier de n mais n//i n'est pas premier, alors
                # n possède au moins 3 diviseurs premiers.
                break

        i += 1

    if not trouve:
        print("Le nombre {} ne peut pas être factorisé en deux nombres premiers.".format(n))


if __name__ == '__main__':
    trouver_deux_facteurs_premiers(42)
    trouver_deux_facteurs_premiers(77)
    trouver_deux_facteurs_premiers(91)
