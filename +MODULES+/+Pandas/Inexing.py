1import pandas as pd
from colorama import init, Fore
import datetime

init()
print(Fore.GREEN, 'Зчитані дані')
Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Frame, '\n')

print('Новий рядок')
Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)  # Новий рядок
print(Frame, '\n')

print('Новий стовпець')
Frame['Birth'] = ['04.11.1998'] + ['01.01.1998'] * 3  # Новий стовпець
Frame['Sex'] = [None] * 4
print(Frame, '\n')

'---------------new------------------'
print('Зміна типу подачі дати')
Frame.Birth = Frame.Birth.apply(pd.to_datetime)  # Зміна типу подачі дати
print(Frame, '\n')

print('Тип обєкта')
print(Frame.dtypes, '\n')  # Тип обєкта

print('Повна інформація')
print(Frame.info(), '\n')  # Повна інформація

print('Заповнення пустих значень {None} новими {Man}')
Frame.fillna('Man', inplace=True)  # Заповнення пустих значень {None} новими {'Man'}
print(Frame, '\n')

print('Вивід стовця як масива')
print(Frame.Sex, '\n')  # Вивід стовця як масива

print('Вивід стовця як таблиці')
print(Frame[['Sex']], '\n')  # Вивід стовця як таблиці

print('Вивід перших двох рядків т-ці')
print(Frame.head(2), '\n')  # Вивід перших двох рядків т-ці
# або print(Frame[:2])
print('Вивід двох останіх рядків т -ці')
print(Frame[-2:], '\n')  # Вивід двох останіх рядків т -ці

print('Розширеий вивід бажаних стовців і рядків (за назвами )')
print(Frame.loc[[0, 2], ['Name', 'Sex']], '\n')  # Розширеий вивід бажаних стовців і рядків (за назвами)
print('Розширеий вивід бажаних стовців і рядків (за номерами)')
print(Frame.iloc[[0, 2], [0, 3]], '\n')  # Розширеий вивід бажаних стовців і рядків (за номерами)

print('Сортування по даті через {import datetime}')
print(Frame[Frame.Birth >= datetime.datetime(1998, 4, 11)], '\n')  # Сортування по даті через {import datetime}

print('Обєднання умов виведення т-ці')
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) & (Frame.Sex == 'Man')],
      '\n')  # Обєднання умов виведення т-ці

print('Або')
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) | (Frame.Sex == 'Man')],
      '\n')  # 'Або'
input()
