L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

somme = 1

for valeur in L:
    if valeur >= 25 and valeur <= 90:
        somme *= valeur

print(somme)