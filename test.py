import csv
import random

def read_data(file_path: str, delimiter: str) -> list:
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            if row:  # Проверка на пустую строку
                data.append(row)
    return data
    
def choose_one_row(data_table: list, type: str = 'clothes') -> list:
    # Фильтруем строки по заданному типу
    filtered_data = [row for row in data_table if row[0].strip() == type]
    
    if not filtered_data:
        return None  # Если нет данных для заданного типа, возвращаем None
    # Выбираем случайный элемент из отфильтрованных данных
    random_item = random.choice(filtered_data)
    return random_item


shop_data = read_data('data/shop_names.csv',delimiter=';')
print(shop_data)
random_row = choose_one_row(data_table=shop_data, type='clothes')

print(random_row)