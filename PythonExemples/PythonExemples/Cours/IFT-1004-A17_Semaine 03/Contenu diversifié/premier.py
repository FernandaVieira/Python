# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Décomposition fonctionnelle

def diviseur(a, b):
    return a % b == 0

def premier(n):
    est_premier = True
    candidat = 2

    while candidat <= n - 1 and est_premier == True:
        if diviseur(n, candidat):
            est_premier = False
        candidat += 1 # équivalent à: candidat = candidat + 1
    
    return est_premier

print( premier(2) )  # True
print( premier(5) )  # True
print( premier(7) )  # True
print( premier(15) ) # False
print( premier(10) ) # False

x = 13
if premier(x):
    print('{} est premier.'.format(x))
else:
    print("{} n'est pas premier.".format(x))
