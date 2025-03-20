import os
os.system('cls')
print("\n")

#1.uzdevums
# text = input("Ievadi tekstu :")
# print(text[-5:])

#2.uzdevums
# sk = input("ievadi skaitli:")
# x = sk 
# for x in range(20):
#     if x %3 ==0:
#         continue
#     print(x)
#     if x ==15:
#         break
    

#3.uzdevums
# x = int(input("ievadi skaitli:"))
# n =[x,
#      x-1,
#      x-2,
#      x-3,
#      x-4,
#      x-5,
#      x-6,
#      x-7,
#      x-8,
#      x-9,
#      x-10
#      ] 
# for i in n:
#     print(i)
     
     



#4.uzdevums
# dict = {"Anna": 20, "Jānis": 22,"Ilze": 19, "Artūrs": 28, "Edgars": 45}
# name= input("ievadi vārdu ko vēlies atrast:")
# print(dict.get(name))

#5.uzdevums
import time

import sys

laiks = int(input("Ievadiet lejupskaitīšanas laiku sekundēs: "))

while laiks > 0:

     minutes = laiks // 60

     sekundes = laiks % 60

     sys.stdout.write(f"\r{minutes:02}:{sekundes:02}")

     sys.stdout.flush()

     time.sleep(1)

     laiks -= 1

sys.stdout.write("\r Kontroldarbs beidzies! \n")

