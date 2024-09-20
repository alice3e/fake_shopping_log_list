import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox, Progressbar
import threading
import tkthread
import random
import csv
from datetime import datetime, timedelta
import os
import select

# Инициализируем tkthread
tkthread.patch()


possible_brands = []
possible_shopname = []
possible_item_and_price = []
possible_bank_system = []
bank_names = ['GAZPROMBANK','MTS BANK','SBERBANK OF RUSSIA','TINKOFF BANK','VTB BANK']
painment_system_names = ['MIR','VISA','MASTERCARD']
progress_bar = None


# Функция для обновления прогресс-бара
def update_progress(current_value, total):
    progress = (current_value / total) * 100
    progress_bar['value'] = progress

# Основная функция для генерации данных
def generate_dataset(amount=50, category_type=1, possibility_banks=[0.5,0.1,0.1,0.1,0.1,0.1], possibility_painment_sys=[0.5,0.1,0.1,0.1,0.1,0.1]):
    if category_type == 4:
        for i in range(1, 4):
            generate_possible_variants(i)
    else:
        generate_possible_variants(category_type)
    generate_card_dataset()
    
    progress_amount = max(1, amount // 100)  # Делим на 100, чтобы не было слишком частого обновления

    for i in range(amount):
        if i % progress_amount == 0:
            # Обновляем прогресс через tkthread, чтобы обновление происходило в главном потоке
            tkthread.run(lambda: update_progress(i, amount))
        
        out = generate_one_output(poss_bank_vec=possibility_banks, poss_painment_vec=possibility_painment_sys)
        write_into_csv_file(out)

    # Устанавливаем значение прогресс-бара на 100 по завершении задачи
    tkthread.run(lambda: update_progress(amount, amount))

    # Показываем сообщение о завершении
    tkthread.run(lambda: messagebox.showinfo("Готово", "Создание таблицы завершено"))

# Функция запуска потока
def start_thread():
    possibility_painment_sys = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
    possibility_banks = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
    category_chosen = 1
    amount = 5000  # Количество строк, которое вы хотите генерировать

    # Запуск задачи в отдельном потоке
    threading.Thread(target=generate_dataset, args=(amount, category_chosen, possibility_banks, possibility_painment_sys)).start()

window.mainloop()


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
    t1.place(relx=0.245, rely=0.3)

    t2 = Label(window, text="VISA, %")
    t2.place(relx=0.436, rely=0.3)

    t3 = Label(window, text="MASTERCARD, %")
    t3.place(relx=0.627, rely=0.3)
    
    combo1 = Combobox(window, width=10)  
    combo1['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo1.current(5) 
    combo1.place(relx=0.245, rely=0.37)

    combo2 = Combobox(window, width=10)  
    combo2['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo2.current(1) 
    combo2.place(relx=0.436, rely=0.37)

    combo3 = Combobox(window, width=10)  
    combo3['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo3.current(1) 
    combo3.place(relx=0.627, rely=0.37)
        
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
    
    progress_bar = Progressbar(window, orient=HORIZONTAL, length=500, mode='determinate')
    progress_bar.place(relx=0.5, rely=0.75, anchor=CENTER)  # Разместим его под настройками

    
    def on_button_click():
        possibility_painment_sys = [float(combo1.get())/100,float(combo2.get())/100,float(combo3.get())/100]
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