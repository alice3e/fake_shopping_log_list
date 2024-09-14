import random
import csv
from datetime import datetime, timedelta
import os

possible_brands = []
possible_shopname = []
possible_item_and_price = []

def generate_possible_variants(category=2):
    match category:
        case 1: #electronics
            output = ['electronics'] # product_type, shop_name, category, brand, price
        case 2: #clothes
            output = ['clothes']
        case 3: #food
            output = ['food']
        case 3: #all types
            output = ['all_types']
    
    with open('data/shop_names.csv',mode='r') as shops_csv:
        line_count = 0
        for rows in shops_csv:
            if line_count==0 or rows[0] =='\t':
                pass
            else:
                shop_name,product_type, = rows.split('\t')
                product_type = product_type[:-1]
                if(product_type==output[0] or output[0]=='all_types'):
                    possible_shopname.append(shop_name)
            line_count += 1
    with open('data/brands.csv',mode='r') as brands_csv:
        line_count = 0
        for rows in brands_csv:
            if line_count==0 or rows[0] =='\t':
                pass
            else:
                product_type,brand_name = rows.split('\t')
                brand_name = brand_name[:-1]
                if(product_type==output[0] or output[0]=='all_types'):
                    possible_brands.append(brand_name)
            line_count += 1
    with open('data/products.csv',mode='r') as item_csv:
        line_count = 0
        for rows in item_csv:
            if line_count==0 or rows[0] =='\t':
                pass
            else:
                product_type,item_type,min_price,max_price = rows.split('\t')
                print(product_type,item_type,min_price,max_price)
                max_price = max_price[:-1]
                min_price = float(min_price) * 43
                max_price = float(max_price) * 43
                if(product_type==output[0] or output[0]=='all_types'):
                    possible_item_and_price.append([item_type,min_price,max_price])
            line_count += 1
            
def dms_to_decimal(deg, minutes, sec, direction):
    decimal = deg + minutes / 60 + sec / 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# точки для генерации координат
A = [dms_to_decimal(59, 57, 28.1, 'N'), dms_to_decimal(30, 18, 30.5, 'E')]
B = [dms_to_decimal(59, 50, 17.6, 'N'), dms_to_decimal(30, 11, 58.1, 'E')]
C = [dms_to_decimal(59, 53, 32.8, 'N'), dms_to_decimal(30, 31, 0.9, 'E')]

def generate_coordinates():
    r1 = random.random()
    r2 = random.random()
    
    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2
    
    coord_N = A[0] + r1 * (B[0] - A[0]) + r2 * (C[0] - A[0])
    coord_E = A[1] + r1 * (B[1] - A[1]) + r2 * (C[1] - A[1])
    coord_N = round(coord_N, 8)
    coord_E = round(coord_E, 8)

    return (str(coord_N) + ' ; ' + str(coord_E))

def generate_random_datetime(min_time="09:00", max_time="21:00"):
    # Задаем диапазон дат: начальная и конечная
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Вычисляем количество дней между начальной и конечной датами
    time_between_dates = end_date - start_date
    total_days = time_between_dates.days
    
    # Генерируем случайный день в пределах диапазона
    random_days = random.randint(0, total_days)
    random_date = start_date + timedelta(days=random_days)
    
    # Преобразуем минимальное и максимальное время в объекты time
    min_time_obj = datetime.strptime(min_time, "%H:%M").time()
    max_time_obj = datetime.strptime(max_time, "%H:%M").time()
    
    # Генерируем случайное время в пределах указанного диапазона
    min_seconds = min_time_obj.hour * 3600 + min_time_obj.minute * 60
    max_seconds = max_time_obj.hour * 3600 + max_time_obj.minute * 60
    random_seconds = random.randint(min_seconds, max_seconds)
    
    # Преобразуем случайное количество секунд в объект времени
    random_time = (datetime.min + timedelta(seconds=random_seconds)).time()
    
    # Соединяем случайную дату и время
    random_datetime = datetime.combine(random_date, random_time)
    
    # Возвращаем дату и время в формате ISO 8601: YYYY-MM-DDTHH:MM
    return random_datetime.strftime("%Y-%m-%dT%H:%M")

def generate_one_output():
    #['спортмастер', [59.86569725, 30.24353742], '2024-08-28T15:44', 'Балетки', 'Prada', 1373173076729863, 6, 3871]
    # brand_name    coordinates                   time              item_type   brand_name  unique_id   amount  price
    out = []
    out.append(random.choice(possible_shopname)) # brand
    out.append(generate_coordinates()) # coordinates
    item,min_pr,max_pr = random.choice(possible_item_and_price)
    print(item,min_pr,max_pr)
    min_time = '0'+str(random.randint(7,9))+':00'
    max_time =  str(random.randint(19,22))+':00'
    out.append(generate_random_datetime(min_time=min_time,max_time=max_time))
    out.append(item)
    out.append(random.choice(possible_brands)) # TODO : add 500 brands
    out.append(random.randint(1000000000000000,9999999999999999)) # TODO : change bank card algorithm with no more than 5 reps
    amount = random.randint(1,7)
    out.append(amount)
    out.append(random.randint(min_pr,max_pr) * amount)
    return out

def write_into_csv_file(sample):
    # Названия столбцов
    headers = ['Магазин', 'Координаты', 'Дата и время', 'Товар', 'Производитель', 'Номер карты', 'Количество', 'Цена']
    
    # Проверяем, существует ли файл result.csv
    file_exists = os.path.isfile('output/result.csv')
    
    # Открываем CSV файл для записи или создания
    with open('output/result.csv', mode='a', newline='', encoding='utf-8') as out_csv:
        # Создаем объект writer
        writer = csv.writer(out_csv, delimiter=',')
        
        # Если файл не существует, записываем заголовки
        if not file_exists:
            writer.writerow(headers)
        
        # Записываем переданный массив данных
        writer.writerow(sample)

def generate_dataset(amount=5, category_type=1): # TODO : check for unique values
    generate_possible_variants(category_type)
    for i in range(amount):
        if(i % 10000 == 0):
            print(f'working, {round(((i/amount)*100),1)}%')
        out = generate_one_output()
        write_into_csv_file(out)


if __name__ == '__main__':

    print("Добро пожаловать в программу генерации синтетических данных")
    amount = int(input('Введите нужное количество записей в базу данных: '))
    generate_dataset(amount=amount,category_type=3)
    print("Готово, проверьте файл result.csv")