import os
os.system('cls')
print("\n")

# x = int(input("Kāda ir x vērtība?"))
# y = int(input("Kāda ir y vērtība?"))

# if x < y:
#     print("x ir mazāks par y")
# elif x > y:
#     print("x ir lielāks par y")
# elif x == y:
#     print("x ir vienāds ar y")

punkti = int(input("Punkti: "))

if punkti >= 90 and punkti <=100:
     print("Vērtējums: 10")
elif punkti >=80 and punkti <90:
    print("Vērtējums: 9")
elif punkti >=70 and punkti <80:
     print("Vērtējums: 8")

# import math
# a = int(input("Kāda vērtība ir a?"))
# b = int(input("Kāda ir vērtība b?"))
# c = int(input("Kāda ir vērtība c?"))
# D=b**2 - 4*a*c
# if D < 0:
#     print("Šeit nav sakņu. Ilgi domāju")
