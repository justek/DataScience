file = "model_results_2024_Q3.csv"
split_file = file.split("_")
model_name = split_file[0]
year = split_file[2]
quarter = split_file[3].split(".")[0]
is_csv = file.endswith('.csv')
print(f"Model: {model_name}, Year: {year}, Quarter: {quarter}")
print(f"Czy to plik csv? {is_csv}")