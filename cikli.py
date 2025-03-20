import os
os.system('cls')
print("\n")

#1.Perfekti skaitļi

for sk in range(1,10000):
    summa = 0
    for i in range(1,sk):
        if sk % i ==0:
            summa = summa + i
    if summa == sk:
        print(f"{sk} ir perfekts skaitlis")    

#2.Skaitļu piramīda
# n = int(input("skaits?"))
# rinda = 1
# while rinda < n:
#     for i in range(1,rinda):
#         print(i)
#     rinda += 1



