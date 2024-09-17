from bs4 import BeautifulSoup
import csv

def parse_html_to_csv(html_file, output_csv):
    # Открываем и читаем содержимое HTML файла
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Ищем все строки таблицы с нужным классом
    rows = soup.find_all('tr', class_='even:bg-opacity-50 even:bg-slate-50 dark:even:bg-opacity-10')

    # Открываем CSV файл для записи
    with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Проходимся по строкам и извлекаем данные
        for row in rows:
            data = []
            # Ищем все ячейки в строке
            cells = row.find_all('td')
            for cell in cells:
                # Получаем текст внутри ячейки и убираем лишние пробелы
                cell_text = cell.get_text(strip=True)
                data.append(cell_text)
            
            # Записываем строку данных в CSV
            if data:
                csv_writer.writerow(data)

# Пример использования
parse_html_to_csv('cards/vtb_card.html', 'cards/cards.csv')
