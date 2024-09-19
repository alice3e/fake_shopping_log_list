from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import select

def clicked():
    try:
        size = int(txt.get())
    except:
        size = 1000
    if ((int(combo1.get()) + int(combo2.get()) + int(combo3.get())) != 100) or ((int(combo4.get()) + int(combo5.get()) + int(combo6.get()) + int(combo7.get())) != 100):
        messagebox.showinfo('Ошибка', 'Сумма в процентах не равна 100')    
    else:
        gen_dataset(int(combo1.get()), int(combo2.get()), int(combo3.get()), int(combo4.get()), 
                    int(combo5.get()), int(combo6.get()), int(combo7.get()), size)
        messagebox.showinfo('Готово', 'Создание таблицы завершено')

if __name__ == '__main__':
    window = Tk()
    window.title("Конструктор синтетических данных")
    window.geometry('500x400')

    # Labels
    lbl = Label(window, text="Добро пожаловать!", font='Arial 16 bold')  
    lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

    lbl2 = Label(window, text="Перед началом работы выберите необходимые настройки:", font='Arial 12')  
    lbl2.place(relx=0.5, rely=0.17, anchor=CENTER)

    # Payment system processing:
    lbl3 = Label(window, text="Платежная система:", font='Arial 11')
    lbl3.place(relx=0.5, rely=0.25, anchor=CENTER)

    t1 = Label(window, text="MasterCard, %")
    t1.place(relx=0.044, rely=0.3)

    t2 = Label(window, text="Visa, %")
    t2.place(relx=0.44, rely=0.3)

    t3 = Label(window, text="Мир, %")
    t3.place(relx=0.79, rely=0.3)

    combo1 = Combobox(window, width=10)  
    combo1['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo1.current(3) 
    combo1.place(relx=0.05, rely=0.37)

    combo2 = Combobox(window, width=10)  
    combo2['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo2.current(3) 
    combo2.place(relx=0.4, rely=0.37)

    combo3 = Combobox(window, width=10)  
    combo3['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
    combo3.current(1) 
    combo3.place(relx=0.75, rely=0.37)

    # Bank processing:
    lbl4 = Label(window, text="Банк:", font='Arial 11')
    lbl4.place(relx=0.5, rely=0.5, anchor=CENTER)

    t4 = Label(window, text="Сбербанк, %")
    t4.place(relx=0.044, rely=0.57)

    t5 = Label(window, text="Тинькофф, %")
    t5.place(relx=0.3, rely=0.57)

    t6 = Label(window, text="ВТБ, %")
    t6.place(relx=0.57, rely=0.57)

    t7 = Label(window, text="Альфа-банк, %")
    t7.place(relx=0.75, rely=0.57)

    combo4 = Combobox(window, width=10)  
    combo4['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo4.current(2) 
    combo4.place(relx=0.05, rely=0.65)

    combo5 = Combobox(window, width=10)  
    combo5['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo5.current(2) 
    combo5.place(relx=0.3, rely=0.65)

    combo6 = Combobox(window, width=10)  
    combo6['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo6.current(2) 
    combo6.place(relx=0.53, rely=0.65)

    combo7 = Combobox(window, width=10)  
    combo7['values'] = (10, 20, 30, 40, 50, 60, 70)  
    combo7.current(0) 
    combo7.place(relx=0.75, rely=0.65)

    txt = Entry(window,width=20)  
    txt.place(relx=0.2, rely=0.85)

    lbl9 = Label(window, text="Введите количество строк", font='Arial 12')
    lbl9.place(relx=0.3, rely=0.8, anchor=CENTER)

    lbl11 = Label(window, text="Значение по умолчанию: 10000", font='Arial 8')
    lbl11.place(relx=0.3, rely=0.95, anchor=CENTER)

    btn = Button(window, text="Создать таблицу", command=clicked)
    btn.place(relx=0.95, rely=0.95, anchor="se", width=150) 

    window.mainloop()