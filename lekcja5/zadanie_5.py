linia = "Alice,28,Data Scientist,75000"
linia_split = linia.split(",")
imie = linia_split[0]
wiek = int(linia_split[1])
zawod = linia_split[2]
zarobki = float(linia_split[3])
print(f"{imie} ma {wiek} lat, pracuje jako {zawod} i zarabia ${int(zarobki)}")