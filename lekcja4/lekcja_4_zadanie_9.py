minimum = 50
maximum = 100

wartosci = [75, 50, 100, 62.5]

print("Wartość | Znormalizowana")

for value in wartosci:
    normalized = (value - minimum) / (maximum - minimum)

    if 0 <= normalized <= 1:
        print(f"{value} | {normalized:.2f}")
    else:
        print(f"{value} | Poza zakresem")