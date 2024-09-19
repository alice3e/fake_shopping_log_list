import random
import csv
from datetime import datetime, timedelta
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import select

possible_brands = []
possible_shopname = []
possible_item_and_price = []
possible_bank_system = []
bank_names = ['GAZPROMBANK','MTS BANK','SBERBANK OF RUSSIA','TINKOFF BANK','VTB BANK']
painment_system_names = ['MIR','VISA','MASTERCARD','MAESTRO','AMERICAN EXPRESS']

def generate_possible_variants(category):
    match category:
        case 1: #electronics
            output = ['electronics'] # product_type, shop_name, category, brand, price
        case 2: #clothes
            output = ['clothes']
        case 3: #food
            output = ['food']
    try:
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
    except:
        print("No shop_names.csv found, exiting..,")
        exit()
    try:
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
    except:
        print("No brands.csv found, exiting..,")
        exit()
    try:
        with open('data/products.csv',mode='r') as item_csv:
            line_count = 0
            for rows in item_csv:
                if line_count==0 or rows[0] =='\t':
                    pass
                else:
                    product_type,item_type,min_price,max_price = rows.split('\t')
                    #max_price = max_price[:-1]
                    try:
                        min_price = int(float(min_price) * 43)
                        max_price = int(float(max_price) * 43)
                    except:
                        print("Problems with price generation in generate_possible_variants")
                        exit()
                    if(product_type==output[0] or output[0]=='all_types'):
                        possible_item_and_price.append([item_type,min_price,max_price])
                line_count += 1
    except:
        print("No products.csv found, exiting..,")
        exit()
            
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

def generate_10_digits():
    return random.randint(1000000000,9999999999)

def generate_card_dataset():
    with open('data/cards.csv',mode='r') as cards_csv:
        line_count = 0
        for rows in cards_csv:
                if line_count==0 or rows[0] =='\t':
                    pass
                else:
                    bin, country, bank_name, system_name, card_type, tariff = rows.split(',')
                    possible_bank_system.append([bin,bank_name,system_name])
                line_count += 1
                    
def generate_one_card(bank='random', system='random'):
    cards = possible_bank_system
    
        # Фильтруем карты по банку
    filtered_cards = [card for card in cards if (bank == 'random' or card[1] == bank) and (system == 'random' or card[2] == system)]
    
    # Если есть подходящие карты, возвращаем случайную
    if filtered_cards:
        chosen_card_start = random.choice(filtered_cards)
        chosen_BIN = str(chosen_card_start[0])
        return (chosen_BIN[:-1]+str(generate_10_digits()))
    else:
        return None
    
def possibility_generator(poss_vec, cat_vec):
    probabilities = poss_vec
    return random.choices(cat_vec, probabilities)[0]

def generate_one_output(poss_bank_vec,poss_painment_vec):
    out = []
    out.append(random.choice(possible_shopname)) # brand
    out.append(generate_coordinates()) # coordinates
    item,min_pr,max_pr = random.choice(possible_item_and_price) # price
    min_time = '0'+str(random.randint(7,9))+':00' # time
    max_time =  str(random.randint(19,22))+':00' # time
    out.append(generate_random_datetime(min_time=min_time,max_time=max_time)) # time
    out.append(item) 
    out.append(random.choice(possible_brands))
    bank,painment_sys = possibility_generator(poss_bank_vec, bank_names),possibility_generator(poss_painment_vec, painment_system_names)
    out.append(generate_one_card(bank=bank,system=painment_sys)) # card generation
    amount = random.randint(1,7) # amount of items
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

def generate_dataset(amount=50, category_type=1, possibility_banks=[0.5,0.1,0.1,0.1,0.1,0.1], possibility_painment_sys=[0.5,0.1,0.1,0.1,0.1,0.1]):
    if(category_type==4):
        for i in range(1,4):
            generate_possible_variants(i)
    else:
        generate_possible_variants(category_type)
    generate_card_dataset()
    for i in range(amount):
        if(i % 10000 == 0):
            print(f'working, {round(((i/amount)*100),1)}%')
        out = generate_one_output(poss_bank_vec=possibility_banks,poss_painment_vec=possibility_painment_sys)
        write_into_csv_file(out)

def clicked(possibility_banks,possibility_painment_sys,category_type):
    try:
        amount = int(txt.get())
    except:
        amount = 1000
    if ((sum(possibility_banks)) != 1.0) or (sum(possibility_painment_sys) != 1.0):
        messagebox.showinfo('Ошибка', 'Сумма в процентах не равна 100')    
    elif(amount <= 0):
        messagebox.showinfo('Ошибка', 'Указано неправильное количество строк')    
    else:
        generate_dataset(amount=amount, category_type=category_type, possibility_banks=possibility_banks, possibility_painment_sys=possibility_painment_sys)
        messagebox.showinfo('Готово', 'Создание таблицы завершено')


if __name__ == '__main__':
    window = Tk()
    window.title("Конструктор синтетических данных")
    window.geometry('900x600')

    # Labels
    lbl = Label(window, text="Добро пожаловать!", font='Arial 16 bold')  
    lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

    lbl2 = Label(window, text="Перед началом работы выберите необходимые настройки:", font='Arial 12')  
    lbl2.place(relx=0.5, rely=0.17, anchor=CENTER)

    # Payment system processing:
    lbl3 = Label(window, text="Платежная система:", font='Arial 11')
    lbl3.place(relx=0.5, rely=0.25, anchor=CENTER)

    #['MIR','VISA','MASTERCARD','MAESTRO','AMERICAN EXPRESS']
    t1 = Label(window, text="MIR, %")
    t1.place(relx=0.045, rely=0.3)

    t2 = Label(window, text="VISA, %")
    t2.place(relx=0.236, rely=0.3)

    t3 = Label(window, text="MASTERCARD, %")
    t3.place(relx=0.427, rely=0.3)
    
    t4 = Label(window, text="MAESTRO, %")
    t4.place(relx=0.618, rely=0.3)
    
    t5 = Label(window, text="AMERICAN EXPRESS, %")
    t5.place(relx=0.809, rely=0.3)

    combo1 = Combobox(window, width=10)  
    combo1['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo1.current(5) 
    combo1.place(relx=0.045, rely=0.37)

    combo2 = Combobox(window, width=10)  
    combo2['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo2.current(0) 
    combo2.place(relx=0.236, rely=0.37)

    combo3 = Combobox(window, width=10)  
    combo3['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo3.current(0) 
    combo3.place(relx=0.427, rely=0.37)
    
    combo4 = Combobox(window, width=10)  
    combo4['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo4.current(0) 
    combo4.place(relx=0.618, rely=0.37)
    
    combo5 = Combobox(window, width=10)  
    combo5['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo5.current(0) 
    combo5.place(relx=0.809, rely=0.37)

    # Bank processing:
    lbl4 = Label(window, text="Банк:", font='Arial 11')
    lbl4.place(relx=0.5, rely=0.5, anchor=CENTER)

    #['GAZPROMBANK','MTS BANK','RENAISSANCE CREDIT','SBERBANK OF RUSSIA','TINKOFF BANK','VTB BANK']
    t6 = Label(window, text="GAZPROMBANK, %")
    t6.place(relx=0.045, rely=0.57)

    t7 = Label(window, text="MTS BANK, %")
    t7.place(relx=0.236, rely=0.57)

    t8 = Label(window, text="VTB, %")
    t8.place(relx=0.427, rely=0.57)

    t9 = Label(window, text="SBERBANK, %")
    t9.place(relx=0.618, rely=0.57)
    
    t10 = Label(window, text="TINKOFF, %")
    t10.place(relx=0.809, rely=0.57)
    
    combo6 = Combobox(window, width=10)  
    combo6['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo6.current(5) 
    combo6.place(relx=0.045, rely=0.65)

    combo7 = Combobox(window, width=10)  
    combo7['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo7.current(0) 
    combo7.place(relx=0.236, rely=0.65)

    combo8 = Combobox(window, width=10)  
    combo8['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo8.current(0) 
    combo8.place(relx=0.427, rely=0.65)

    combo9 = Combobox(window, width=10)  
    combo9['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo9.current(0) 
    combo9.place(relx=0.618, rely=0.65)
    
    combo10 = Combobox(window, width=10)  
    combo10['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo10.current(0) 
    combo10.place(relx=0.809, rely=0.65)

    txt = Entry(window,width=20)  
    txt.place(relx=0.2, rely=0.85)

    lbl9 = Label(window, text="Введите количество строк", font='Arial 12')
    lbl9.place(relx=0.3, rely=0.8, anchor=CENTER)

    lbl11 = Label(window, text="Значение по умолчанию: 10000", font='Arial 8')
    lbl11.place(relx=0.3, rely=0.95, anchor=CENTER)


    lbl12 = Label(window, text="Выберите категорию товаров", font='Arial 12')
    lbl12.place(relx=0.6, rely=0.8, anchor=CENTER)
    
    combo11 = Combobox(window, width=20)  
    combo11['values'] = ('electronics','clothes','food','all types')  
    combo11.current(3) 
    combo11.place(relx=0.5, rely=0.85)
    
    def on_button_click():
        possibility_painment_sys = [float(combo1.get())/100,float(combo2.get())/100,float(combo3.get())/100,float(combo4.get())/100,float(combo5.get())/100]
        possibility_banks = [float(combo6.get())/100,float(combo7.get())/100,float(combo8.get())/100,float(combo9.get())/100,float(combo10.get())/100]
        category_chosen = combo11.get()
        category_id = {
            'electronics': 1,
            'clothes': 2,
            'food': 3,
            'all types': 4
        }
        print(category_id[category_chosen])
        clicked(possibility_banks=possibility_banks, possibility_painment_sys=possibility_painment_sys, category_type=category_id[category_chosen])

    btn = Button(window, text="Создать таблицу", command=on_button_click)
    btn.place(relx=0.95, rely=0.95, anchor="se", width=150) 

    window.mainloop()