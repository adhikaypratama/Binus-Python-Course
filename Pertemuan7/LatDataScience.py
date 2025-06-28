import pandas as pd

df = pd.read_csv('Negara.csv', index_col=0)
meanLuas = df.Luas.mean()
stdLuas = df.Luas.std()
meanPopulasi = df.Populasi.mean()
stdPopulasi = df.Populasi.mean()

print(df)
print("Mean Luas: ", meanLuas)
print("Standar Deviasi Luas: ", stdLuas)
print("Mean Populasi: ", meanPopulasi)
print("Standar Deviasi Populasi: ", stdPopulasi)
