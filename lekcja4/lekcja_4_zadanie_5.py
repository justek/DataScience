sciezka = "data/processed/train_fold_03_normalized.csv"

elementy_sciezki = sciezka.split("/")
folder = elementy_sciezki[1]

nazwa_pliku = elementy_sciezki[2].split("_")
typ_zbioru = nazwa_pliku[0]
numer_fold = nazwa_pliku[2]
format_pliku = nazwa_pliku[3].split(".")[1]

print("Folder:", folder)
print("Typ zbioru:", typ_zbioru)
print("Numer fold:", numer_fold)
print("Format pliku:", format_pliku)