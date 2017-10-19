# Auteur: Honore Hounwanou <mercuryseries@gmail.com>
# Description: Les structures conditionnelles (La forme if-elif-else)

# Exemple 1
note = 15

if note >= 18:
    print('Très bien')
elif note >= 14:
    print('Pas mal')
elif note >= 10:
    print('Passable')
elif note >= 5:
    print('Je salue ton effort.')
else:
    print(':(')

print('Je suis une chaîne de caractères qui sera toujours affichée.')

# Exemple 2 (Imbrication de conditions)
note = 9

if note >= 18:
    print('Très bien')
elif note >= 14:
    print('Pas mal')
elif note >= 10:
    print('Passable')
else:
    if note >= 5:
        print('Je salue ton effort.')
    else:
        print(':(')

print('Je suis une chaîne de caractères qui sera toujours affichée.')
