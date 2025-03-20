
string = input ("Ievadi simbolu virkni:")
print(f"Simbolu virknes garums: {len(string)}")

print(f"Virkne ar lielajiem burtiem: {string.upper()}")
print(f"Virkne ar mazajiem burtiem: {string.lower()}")

symbol = input ("ievadi simbolu, ko lietot tukšo vietu aizvietošanai: ")
print(f"Aizvietot arstarpes: {string.replace(' ', symbol)}")

word_to_check = "Python"
print(f"Vai virkne satur vārdu '{word_to_check}'? {'Python' in string}")

