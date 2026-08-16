celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F = {kelvin:.1f} K")
