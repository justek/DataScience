from statistics import fmean, pstdev

wagi = [65.5, 78.2, 54.8, 92.1, 70.0]

srednia = fmean(wagi)
odchylenie_standardowe = pstdev(wagi)
z_score = [(waga - srednia) / odchylenie_standardowe for waga in wagi]

def interpretuj(z):
    if z > 2:
        return "wartość bardzo wysoka"
    if z < -2:
        return "wartość bardzo niska"
    if abs(z) <= 1:
        return "wartość typowa"
    return "wartość nieco nietypowa"

print(f"Średnia wag: {srednia:.2f} kg")
print(f"Odchylenie standardowe: {odchylenie_standardowe:.2f} kg\n")
print("Waga (kg) | Z-score | Interpretacja")

for waga, z in zip(wagi, z_score):
    print(f"{waga:9.1f} | {z:7.3f} | {interpretuj(z)}")

print(f"\nŚrednia z-scores: {fmean(z_score):.6f}")
print(f"Odchylenie standardowe z-scores: {pstdev(z_score):.6f}")
