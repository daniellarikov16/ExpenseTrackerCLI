import csv
import os
from tabulate import tabulate
from datetime import datetime

def check_file():
    if not os.path.exists('data.csv'):
        print('Файл не найден, создаем новый')
        data = [['id', 'date', 'description', 'amount']]
        with open('data.csv', mode='w', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print('Файл успешно создан')

def get_data():
    with open('data.csv', newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def add_expense(description, amount):
    check_file()
    data = get_data()
    new_id = len(data)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append([new_id, current_date, description, amount])
    with open('data.csv', mode='w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print('Данные успешно добавлены')

def update_expense(id, field, new_value):
    check_file()
    data = get_data()
    for row in data[1:]:
        if row[0] == str(id):
            if field == 'description':
                row[2] = new_value
            elif field == 'amount':
                row[3] = new_value
            elif field == 'date':
                row[1] = new_value
            break
    else:
        print(f"Запись с ID={id} не найдена")
        return
    with open('data.csv', mode='w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print('Данные успешно обновлены')

def delete_expense(id):
    check_file()
    data = get_data()
    if not (id > len(data) - 1):
        if id == len(data[1:]):
            data.pop(id)
        else:
            data.pop(id)
            for row in data[id:]:
                row[0] = int(row[0]) - 1
        with open('data.csv', mode='w', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print('Данные успешно удалены')
    else:
        print('Введено неверное id')
        return

def show_info():
    check_file()
    data = get_data()
    print(tabulate(data, headers="firstrow"))

def all_amount():
    check_file()
    data = get_data()
    summ = 0
    for elem in data[1:]:
        summ += int(elem[3])
    print(f'Ваши траты: {summ}')
def month_expense(month):
    check_file()
    data = get_data()
    month_data = [['id', 'date', 'description', 'amount']]
    if not(month > 12):
        if month < 10:
            month = '0'+ str(month)
        for elem in data[1:]:
            if elem[1][5:7] == month:
                month_data.append(elem)
    else:
        print('Неправильный номер месяца')
    print(tabulate(month_data, headers="firstrow"))