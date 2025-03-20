import os
os.system('cls')
print

# 1. Vienkārša teksta rakstīšana un lasīšana no faila 
# teksts = input("Ievadi tekstu:")
# with open("text.txt", "w", encoding = "utf8") as ieraksts:
#     ieraksts.write(teksts)

# 2. Rindu skaitīšana failā 
# with open("data (2).txt", "r", encoding = "utf-8") as data:
#     x = len(data.readlines())
#     print(x)

# 3. Vārda sastopamības skaitīšana failā
vards = input("ievadi vārdu:").upper()
with open("vardi.txt", "r", encoding="utf-8") as data:
    x = data.readlines()
mekl = x.count(vards + "\n")
print(f"{vards} parādas {mekl}")

# 4. Datu pievienošana failam 

# 5. Apvienot divus failus, pārmaiņus ierakstot rindas

# 6. Vārdu atkārtošanās skaita noteikšana failā

# 7. Studentu atzīmju analīze no faila

# 8. Liela faila apstrāde un analīze (Augstāks līmenis)

# 9. Faila filtrēšana un jauna faila izveide (Augstāks līmenis)

# 10. Ezeru saraksta izveide RTF failā
