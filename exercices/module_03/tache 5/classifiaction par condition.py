age= int(input("Quel est votre age?: "))
if age < 13:
    print("Enfant")
elif age <= 17:
    print("adolescent")
elif age >= 18 and age <= 64:
    print("adulte")
else:
    print("ainé")