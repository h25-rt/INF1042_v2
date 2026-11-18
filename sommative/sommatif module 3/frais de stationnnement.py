import math
electrique = input ("le vehicule est il electrique? (oui/non):").lower()
duree= float(input("nombre de temps de stationnement ?: "))
heures_entieres = int(duree)
if duree > heures_entieres:
    heures_facturees = heures_entieres + 1
else:
    heures_facturees = heures_entieres
if heures_facturees <= 0:
    prix_avant_rabais = 0.0
elif heures_facturees == 1:
    prix_avant_rabais = 4.0
else:
    prix_avant_rabais = 4.0 + (heures_facturees - 1) * 2.50
if prix_avant_rabais > 20.0:
    prix_avant_rabais = 20.0
if electrique == "oui":
    rabais = prix_avant_rabais * 0.20
else:
    rabais = 0.0
total = prix_avant_rabais - rabais
print("Durée :", duree, "heures")
print("Heures facturées :", heures_facturees)
print("Prix avant rabais :", round(prix_avant_rabais, 2), "$")
print("Rabais véhicule électrique :", round(rabais, 2), "$")
print("Total :", round(total, 2), "$")
print("aurevoir et bonne journée")