import random
opt= ["roche" , "papier", "ciseaux" ]
v=0
d=0
e=0
cu= ""
print ("jeu de peire papier ciseaux ")
while cu != "quitter":
    cu= input ("quel est votre choix? (roche, papier, ciseaux ou quitter ): ").lower()
    if cu==("quitter"):
        print("fin du jeu")
        break
    if cu not in opt:
        print ("choix invalide! veuiller choisir l'un des choix disponible ")
        continue
    cd= random.choice(opt)
    print("l'ordinateur a choisis:", cd)
    if cu ==cd:
        print ("egalité")
        e+=1
    elif cu=="roche" and cd== "ciseaux":
        print("vous avez gagné")
        v+=1
    elif cu=="papier" and cd== "roche":
        print("vous avez gagné")
        v+=1
    elif cu=="ciseaux"and cd== "papier":
        print("vous avez gagné")
        v+=1
    else:
     print("vous avez perdu" )
    d+=1
print ("score final")
print("victoires:", v)
print("defaites",d)
print ("egalité",e)

