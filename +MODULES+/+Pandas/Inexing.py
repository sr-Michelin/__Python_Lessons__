import pandas as pd
from colorama import init, Fore

init()

Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Fore.GREEN, Frame, '\n')
Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)
print(Frame)
