import random
nb_tir=int(input ("nombre de tirage a simuler?:"))
nb_1=0
nb_2=0
nb_3=0
nb_4=0
for i in range (nb_tir):
    tirage=random.randint(1,4)
    if tirage==1:
         nb_1+=1
    elif tirage==2:
        nb_2+=1
    elif tirage==3:
        nb_3+=1
    else:
        nb_4+=1
pct_1 = (nb_1 / nb_tir) * 100
pct_2 = (nb_2 / nb_tir) * 100
pct_3 = (nb_3 / nb_tir) * 100
pct_4 = (nb_4 / nb_tir) * 100
print("resultats de la simulation")
print("Chiffre 1 :", nb_1, "fois (", round(pct_1, 2), "% )")
print("Chiffre 2 :", nb_2, "fois (", round(pct_2, 2), "% )")
print("Chiffre 3 :", nb_3, "fois (", round(pct_3, 2), "% )")
print("Chiffre 4 :", nb_4, "fois (", round(pct_4, 2), "% )")