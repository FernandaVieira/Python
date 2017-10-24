# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Permutation du contenu de deux variables en utilisant
# un peu d'arithmétique

x = 2
y = 9

# Avant permutation
print(x)
print(y)

# Permutation
x = x + y;
y = x - y;
x = x - y;

# Après permutation
print(x)
print(y)
