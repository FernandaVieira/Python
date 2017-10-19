# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Variables

# Affectation
a = 10
print(type(a))
a = 25.0
print(type(a))
a = 45 + 3
print(type(a))

# Casting ou Transtypage (Convertir une variable d'un type donné à un autre)
a = 25
a = float(a)
print(a)
print(type(a))

b = 45.65
print( int(b) ) 
print( type( int(b) ) ) 

c = '45.6'
print(c)
print( int( float(c) ) ) 
print( int(c) ) # Erreur
