import pandas as pd
from colorama import init, Fore

init()
n = 100

D = {'Name': [None] * n,  # Запис словника для таблиці
     'Sname': [None] * n,
     'Lname': [None] * n
     }
frame = pd.DataFrame(D)  # Подача т-ці через словник
print(Fore.RED, 'Вивід т-ці\n', frame, '\n')  # Вивід т-ці

frame_csv = pd.read_csv('CSV1.csv', header=0, sep=';')  # Відкриття csv-ф
print('Відкриття csv-ф\n', frame_csv, '\n')
print(frame_csv.columns)
print('Type:\n', frame_csv.shape, '\n')

fcsv_new_line = {'Name': 'Ivan', 'Sname': 'Golubosh'}  # запис нового рядка для т-ці
frame_csv = frame_csv.append(fcsv_new_line, ignore_index=1)  # доповнення т-ці цим рядком
print('Запис нового рядка для т-ці\n', frame_csv, '\n')

frame_csv['Is_Student?'] = [True] * 3 + [False]  # запис нового стовпця (ключа)
print('Запис нового стовпця (ключа)\n', frame_csv, '\n')

print('Видалення рядків [1,3]\n', frame_csv.drop([1, 3], axis=0), '\n')  # видалення рядків [1,3]

print('Видалення рядків [1,3] глобальним чином inplace=True\n', frame_csv.drop([1, 3], axis=0, inplace=True),
      '\n')  # видалення рядків [1,3] глобальним чином inplace=True

print('Видалення стовпця(-ів) глобальним чином inplace=True\n',
      frame_csv.drop('Is_Student?', axis=1, inplace=False))  # видалення стовпця(-ів) глобальним чином inplace=True

frame_csv.to_csv('CSV_new.csv', header=True, index=None, sep=';')  # запис отрманої таблиці в окремий csv - файл
