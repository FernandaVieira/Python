# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Fonction retournant plusieurs valeurs

def carre_et_cube(x):
    return x ** 2, x ** 3 

carre_de_3, cube_de_3 = carre_et_cube(3)
print(carre_de_3)
print(cube_de_3)
