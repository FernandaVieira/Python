# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Variables locales

def carre(x):
    y = x ** 2
    return y

carre(3)

# La portée des variables x et y est locale.
# Elles ne seront donc pas disponibles à ce niveau
print(x)
print(y)
