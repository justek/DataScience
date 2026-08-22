path = '/data/processed/2024/experiment_42_v3.csv'
split_path = path.split('/')

file_name = split_path[-1]
catalog = '/' + '/'.join(split_path[1:-1])
name_without_extension = file_name[:file_name.rfind('.')]
extension = file_name[file_name.rfind('.'):]
year = split_path[-2]

report = f"""Nazwa pliku:           {file_name:<25}
Katalog:               {catalog:<25}
Nazwa bez rozszerzenia:{name_without_extension:<25}
Rozszerzenie:          {extension:<25}
Rok z katalogu:        {year:<25}"""

print(report)