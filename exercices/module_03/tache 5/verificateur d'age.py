age = int(input("votre age: "))
reponse_billet = input("as tu un  billet? (oui/non): ")
billet = reponse_billet == "oui"
if billet and age >= 18:
    print("acces autoriser")
else:
    print("acces refuser")
