import pandas as pd
from colorama import init, Fore

init()

Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Fore.GREEN, Frame, '\n')

Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)
print(Frame, '\n')

Frame['Birth'] = ['04.11.1998'] + ['01.01.1998'] * 3
print(Frame, '\n')

'---------------new-------------------'
print(Frame.dtypes, '\n')  # Тип обєк

Frame.Birth = Frame.Birth.apply(pd.to_datetime)  #
print(Frame)
