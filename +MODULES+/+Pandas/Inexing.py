import pandas as pd
from colorama import init, Fore
import datetime

init()
print(Fore.GREEN, 'Зчитані дані')
Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Frame, '\n')

print('Новий рядок')
Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)  # Новий рядок
Frame = Frame.append({'Name': 'Yaryna', 'Sname': 'Ostapchuk'},ignore_index=True)
print(Frame, '\n')

print('Новий стовпець')
Frame['Birth'] = ['04.11.1998'] + ['01.01.1998'] * 3 + ['14.05.1999']  # Новий стовпець
Frame['Sex'] = [None] * 4 + ['Female']
print(Frame, '\n')

'---------------new------------------'
print('Заповнення пустих значень {None} новими {Male}')
Frame.fillna('Male', inplace=True)  # Заповнення пустих значень {None} новими {'Male'}
print(Frame, '\n')

print('Зміна типу подачі дати')
Frame.Birth = Frame.Birth.apply(pd.to_datetime)  # Зміна типу подачі дати
print(Frame, '\n')

Frame.to_csv('CSV_new.csv', header=True, index=None, sep=';')

print('Тип обєкта')

print(Frame.dtypes, '\n')  # Тип обєкта

print('Повна інформація')
print(Frame.info(), '\n')  # Повна інформація

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
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) & (Frame.Sex == 'Male')],
      '\n')  # 'i' - oбєднання умов виведення т-ці

print('Або')
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) | (Frame.Sex == 'Female')],
      '\n')  # 'Або'
input()

