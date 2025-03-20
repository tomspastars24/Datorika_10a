import os
os.system('cls')
print("\n")

#1.uzdevums
# produkts =input("Ievadiet produkta nosaukumu:")
# if produkts == "Briseles kāposts" :
#     print("Balstavielu daudzums uz 100g ir 4,4")
# if produkts == "Seleriju saknes":
#     print("Balstavielu daudzums uz 100g ir 4,2")
# if produkts == "Brokoļi":
#     print("Balstavielu daudzums uz 100g ir 3,0")
# if produkts == "Ziedkāposti":
#     print("Balstavielu daudzums uz 100g ir 2,9")
# if produkts == "Burkāni":
#     print("Balstavielu daudzums uz 100g ir 2,9")
# if produkts == "Sarkanās bietes":
#     print("Balstavielu daudzums uz 100g ir 2,5")
# if produkts == "Salāti":
#     print("Balstavielu daudzums uz 100g ir 1,8")
# if produkts == "Upenes":
#     print("Balstavielu daudzums uz 100g ir 6,8")
# if produkts == "Avenes":
#     print("Balstavielu daudzums uz 100g ir 5,0")
# if produkts == "Zemenes":
#     print("Balstavielu daudzums uz 100g ir 4,0")
# if produkts == "Jāņogas":
#     print("Balstavielu daudzums uz 100g ir 2,5")
# if produkts == "Āboli":
#     print("Balstavielu daudzums uz 100g ir 2,3")
# if produkts == "Apelsīni":
#     print("Balstavielu daudzums uz 100g ir 2,2")
# if produkts == "Plūmes":
#     print("Balstavielu daudzums uz 100g ir 1,7")

#2.uzdevums
# vārds = input("Ieavadi tekstu:")
# patskaņi = "aeiouAEIOU"        
# rezultāts = ""
# for letter in vārds:
#     if letter not in patskaņi:
#         rezultāts += letter
# print("Vārds bez patskaņiem", rezultāts)

#3.uzdevums
cena = 90

summa = 0

nauda=[5,10,20,50]

while summa<cena:

    ievadita_moneta = int(input("Ievieto monētu 5, 10 , 20 vai 50 centi: "))

    if ievadita_moneta in nauda:

        summa += ievadita_moneta

        print(f"Pašlaik ievietotā summa: {summa} centi.")

    else: print("Nederīga moneta. Lūdzu ievadiet 5, 10, 20, 50 centus.")

atlikums = summa - cena

if atlikums > 0:

    print(f"Jāizdod {atlikums} centi.")

        