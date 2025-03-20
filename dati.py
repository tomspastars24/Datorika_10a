import os
os.system('cls')
print('\n')

import pandas
from datetime import datetime
import ctypes

df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)
# print(df)
# print(df.to_string())

input_date = input("Ievadiet datumu (DD.MM): ")

try:

    datetime.strptime(input_date, "%d.%m")

except ValueError:

    print("Nepieņemams datuma formāts. Lūdzu, ievadiet datumu formātā DD.MM.")

    exit()


df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

bd_skoleni = df[df["Dzimšanas datums"] == input_date]

print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas diena!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "šodien nav nevienam dz.diena!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "svinam", 1)