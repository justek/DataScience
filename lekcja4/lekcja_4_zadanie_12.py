liczba_probek = 50_000
batch_size = 128
liczba_epok = 50
czas_na_batch = 0.15

# Uwzględniamy niepełny batch, jeśli po dzieleniu zostaje reszta próbek.
batchy_na_epoke = liczba_probek // batch_size
if liczba_probek % batch_size != 0:
    batchy_na_epoke += 1

calkowity_czas_sekundy = batchy_na_epoke * liczba_epok * czas_na_batch
calkowity_czas_sekundy = round(calkowity_czas_sekundy)

godziny = calkowity_czas_sekundy // 3600
minuty = (calkowity_czas_sekundy % 3600) // 60
sekundy = calkowity_czas_sekundy % 60

print(f"Szacowany czas: {godziny} h {minuty} min {sekundy} s")
