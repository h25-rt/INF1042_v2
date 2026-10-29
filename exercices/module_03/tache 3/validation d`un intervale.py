# Demandez à l'utilisateur de saisir un nombre entier. Si le nombre est supérieur à 0 ET inférieur à 100 (en utilisant l'opérateur logique and), affichez "Nombre valide", sinon affichez "Nombre hors limite".
n= int(input("donner un nombre entier : "))
if n >=0 and n <=100:
    print("nombre valide")
else:
    print("nombre invalide")