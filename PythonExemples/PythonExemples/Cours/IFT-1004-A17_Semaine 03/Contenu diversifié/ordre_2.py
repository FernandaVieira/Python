# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: L'ordre est parfois important 

def diviseur(a, b):
    return a % b == 0

print( premier(2) )
print( premier(5) )

def premier(n):
    est_premier = True
    candidat = 2

    while candidat <= n - 1 and est_premier == True:
        if diviseur(n, candidat):
            est_premier = False
        candidat += 1 # équivalent à: candidat = candidat + 1
    
    return est_premier
