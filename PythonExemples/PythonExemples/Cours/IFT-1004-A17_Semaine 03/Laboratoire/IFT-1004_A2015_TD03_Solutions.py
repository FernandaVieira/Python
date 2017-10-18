"""Solutions du laboratoire 3.

"""


def bissextile_1():
    """Nous vous demandions de ne pas utiliser de fonctions au départ pour fabriquer votre solution.
    Nous vous donnons ici une première solution dans une fonction pour ne pas avoir à vous remettre
    plusieurs fichiers de solution, mais ce code aurait pu être utilisé tel quel à l'extérieur d'une
    fonction.

    Cette solution suit à la lettre les étapes de l'énoncé. Voir plus bas pour une solution simplifiée!

    """
    annee = int(input("Entrez une année (0 pour quitter) : "))
    while annee != 0:

        if annee % 4 == 0:  # Étape 1
            if annee % 100 == 0:  # Étape 2
                if annee % 400 == 0:  # Étape 3
                    print("L'année {} est bissextile.".format(annee))  # Étape 4
                else:
                    print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5
            else:
                print("L'année {} est bissextile.".format(annee))  # Étape 4
        else:
            print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5

        # On demande à nouveau à l'utilisateur, puis la condition de la boucle décidera si on continue ou non.
        annee = int(input("\nEntrez une année (0 pour quitter) : "))


def bissextile_2():
    """Solution alternative simplifiée, utilsant la logique pour combiner ensemble certaines étapes.

    """
    annee = int(input("Entrez une année (0 pour quitter) : "))
    while annee != 0:

        if annee % 4 == 0 and annee % 100 != 0:  # Étapes 1 et 2
            print("L'année {} est bissextile.".format(annee))  # Étape 4
        elif annee % 400 == 0:  # Étape 3
            print("L'année {} est bissextile.".format(annee))  # Étape 4
        else:
            print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5

        annee = int(input("\nEntrez une année (0 pour quitter) : "))


def bissextile_3():
    """Solution alternative encore plus simplifiée, utilsant la logique pour combiner ensemble certaines étapes.

    """
    annee = int(input("Entrez une année (0 pour quitter) : "))
    while annee != 0:

        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:  # Étapes 1, 2 et 3
            print("L'année {} est bissextile.".format(annee))  # Étape 4
        else:
            print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5

        annee = int(input("\nEntrez une année (0 pour quitter) : "))


def bissextile_4():
    """Voici une version qui utilise une boucle infinie (while True), avec une instruction break
    pour quitter la boucle. Notez que le code est un peu plus simple ici.

    """
    while True:
        annee = int(input("\nEntrez une année (0 pour quitter) : "))
        if annee == 0:
            break

        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:  # Étapes 1, 2 et 3
            print("L'année {} est bissextile.".format(annee))  # Étape 4
        else:
            print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5


def bissextile_5():
    """Voici une version utilisant la décomposition fonctionnelle.

    """
    while True:
        annee = demander_annee()
        if annee == 0:
            break

        if est_bissextile(annee):
            print("L'année {} est bissextile.".format(annee))  # Étape 4
        else:
            print("L'année {} n'est pas bissextile.".format(annee))  # Étape 5


def demander_annee():
    """Fonction utilitaire pour bissextile_5.

    """
    return int(input("\nEntrez une année (0 pour quitter) : "))


def est_bissextile(annee):
    """Fonction utilitaire pour bissextile_5. Vérifie si une année passée en paramètres
    est bissextile ou non.

    """
    return (est_divisible(annee, 4) and not est_divisible(annee, 100)) or est_divisible(annee, 400)  # Étapes 1, 2 et 3


def est_divisible(a, b):
    """Fonction utilitaire pour est_bissextile et premier(). Vérifie si le nombre b
    est un diviseur du nombre a.

    """
    return a % b == 0


def premier():
    """Question 2. Notez que la boucle se rend seulement à nombre // 2 au lieu de nombre - 1. Nous pourrions même
    nous arrêter à math.ceil(sqrt(nombre)) !

    """
    nombre = int(input("Entrez un nombre entier : "))

    est_premier = True

    if (nombre == 0 or nombre == 1):
        est_premier = False
    else:
        i = 2
        while i <= nombre // 2 and est_premier:
            if nombre % i == 0:
                est_premier = False
            i = i + 1

    if est_premier:
        print("C'est un nombre premier!")
    else:
        print("Ce n'est pas un nombre premier.")


def table():
    """Question 3.

    """
    x_maximum = int(input("Entrez la valeur de x : "))
    y_maximum = int(input("Entrez la valeur de y : "))
    print()

    # On affiche premièrement la ligne d'en-tête.
    y = 1
    print("    ", end="")
    while y <= y_maximum:
        print("{:4}".format(y), end="")
        y += 1

    # On construit affiche une chaîne de caractères pour délimiter. Nous y reviendrons!
    print()
    print("    -" + "----" * y_maximum)

    # Pour toute valeur de x, on affiche les multiples.
    x = 1
    while x <= x_maximum:

        # Cette instruction permet d'afficher l'en-tête pour la ligne courante.
        print("{:4}|".format(x), end="")

        # Pour toute valeur de y, on affiche les multiplications.
        y = 1
        while y <= y_maximum:
            print("{:4}".format(x * y), end="")
            y += 1  # équivalent à y = y + 1

        print()
        x += 1


if __name__ == '__main__':
    # Point d'entrée principal du programme. Appelez les autres fonctions à partir d'ici !

    # bissextile_1()
    # bissextile_2()
    # bissextile_3()
    # bissextile_4()
    bissextile_5()
    premier()
    table()
