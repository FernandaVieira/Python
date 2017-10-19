# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Variables globales

y = 5

def carre(x):
    y = x ** 2
    return y

carre(3)

print(y) # affichera 5 car ici il est question de la variable globale y.

# Pour rappel, les variables x et y présentes au niveau de la fonction
# carre ont une portée locale. Elles ne seront plus disponibles
# après l'exécution de la fonction.
