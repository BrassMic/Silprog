import pandas as pd
import os

path = os.chdir(input("Ścieżka folderu: "))
list = os.listdir(path)

print(list)
files = list
df = pd.DataFrame()
kol = input("wybierz kolumny: ")
for f in files:
    data = pd.read_excel(f, usecols=kol, index_col=None)
    df = df.append(data)

print(df)
x = input("Nazwa pliku: ")
sheet_name = x + ".xlsx"
engine = 'openpyxl'
writer = pd.ExcelWriter(sheet_name, engine=engine)
df.to_excel(writer)

writer.save()
print("Wszystko poszło jak należy")
