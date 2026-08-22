results = []
results.append(0.75)
results.append(0.82)
results.append(0.79)
results.append(0.85)
results.append(0.88)

length = len(results)
average = sum(results) / length
max_value = max(results)
min_value = min(results)

print(f"Długość listy: {length}")
print(f"Średnia wartość: {average}")
print(f"Maksymalna wartość: {max_value}")
print(f"Minimalna wartość: {min_value}")