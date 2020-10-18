import pandas as pd
from colorama import init, Fore
import datetime

init()

Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Fore.GREEN, Frame, '\n')

Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)  # Новий рядок
print(Frame, '\n')

Frame['Birth'] = ['04.11.1998'] + ['01.01.1998'] * 3  # Новий стовпець
Frame['Sex'] = [None] * 4
print(Frame, '\n')

'---------------new------------------'

Frame.Birth = Frame.Birth.apply(pd.to_datetime)  # Зміна типу подачі дати
print(Frame, '\n')

print(Frame.dtypes, '\n')  # Тип обєкта

print(Frame.info(), '\n')  # Повна інформація

Frame.fillna('Man', inplace=True)  # Заповнення пустих значень {None} новими {'Man'}
print(Frame, '\n')

print(Frame.Sex, '\n')  # Вивід стовця як масива

print(Frame[['Sex']], '\n')  # Вивід стовця як таблиці

print(Frame.head(2), '\n')  # Вивід перших двох рядків т-ці
# або print(Frame[:2])
print(Frame[-2:], '\n')  # Вивід двох останіх рядків т -ці

print(Frame.loc[[0, 2], ['Name', 'Sex']], '\n')  # Розширеий вивід бажаних стовців і рядків (за назвами )
print(Frame.iloc[[0, 2], [0, 3]], '\n')  # Розширеий вивід бажаних стовців і рядків (за номерами)

print(Frame[Frame.Birth >= datetime.datetime(1998, 4, 11)], '\n')  # Сортування по даті через {import datetime}

print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) & (Frame.Sex == 'Man')],
      '\n')  # Обєднання умов виведення т-ці

print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) | (Frame.Sex == 'Man')],
      '\n')  # 'Або'
