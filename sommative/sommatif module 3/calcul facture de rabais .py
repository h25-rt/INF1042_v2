mnt= float(input("quel est le prix avant les taxe?:"))
if mnt < 50:
    rbt= mnt - mnt*0.00
    print("aucun rabais ")
if  mnt >=50:
    rbt= mnt-(mnt* 0.05)
    print(" rabais de 5% ")
elif mnt >100:
    rbt=mnt-mnt* 0.10
    print(" rabais de 10% ")
montant_total = rbt + rbt*0.13
grand_total = montant_total
print("pour un prix de ",mnt,"apliquer d'abotd ",rbt,"avec une  TVH de 13 %. cequi donne un mondant de ",montant_total)