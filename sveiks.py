print("sveiks")
name = input("Kā tevi sauc?")

name = name.strip().title()

pirmais, otrais = name.split(" ")

print("Sveiks,", pirmais)
print(f"Sveiks, {name}")