liczba_probek = 1000

# Proporcje zapisane jako licznik i mianownik, aby użyć dzielenia całkowitego.
zbior_treningowy = liczba_probek * 70 // 100
zbior_walidacyjny = liczba_probek * 15 // 100
zbior_testowy = liczba_probek - zbior_treningowy - zbior_walidacyjny

print("Rozmiar zbioru treningowego:", zbior_treningowy)
print("Rozmiar zbioru walidacyjnego:", zbior_walidacyjny)
print("Rozmiar zbioru testowego:", zbior_testowy)
