
import random
c_p= ["roche", "papier", "ciseaux"]
c_o= random.choice(c_p)
c_u= input("entrer votre choix (roche, papier ou ciseaux) :")
if c_u == c_o:
    print("eaglite")
else:
    print("choix different ")