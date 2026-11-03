taille= int(input("quelle est votre  taille en cm ? : "))
age= int(input("quelle est votre  age  ? : "))
medic= input("avez vous une interdiction (oui/non) ? : ")
if medic == "non" and taille >= 140 or age >= 12 and medic == "non":
    print("acces autoriser")
else:
    print("acces refusé")