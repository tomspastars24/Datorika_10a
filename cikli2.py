import os 
os.system('cls')#attīra termināla logu pašā sākumā
print('\n') # ieliek tukšu rindiņu pirms izdrukas

platums = int(input("platums-"))
augstums = int(input("augstums"))
for i in range(augstums):
    for j in range(platums):
        print("@", end="")
    print()