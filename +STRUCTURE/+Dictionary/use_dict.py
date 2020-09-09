
Mike = {'first name' :'Михайло',
        'middle name':'Сергійович',
        'last name'  :'Шевченко',
        'adress'     : ['м.Львів','вул.Пачічна','буд.62-Б','к.407'],
        'tell'       : '380683168590'}

print('Adress of Mike - ',Mike['adress'])

del Mike['tell']

print('\nNEW number of keys - {0} '.format(len(Mike)))   # Кількість ключів

for key,name in Mike.items():
    print('Key {0} with meaning {1}'.format(key,name))   # Запис ключів із їх значеннями

Mike['tell'] = '380683168590'
if 'tell' in Mike:
    print('\nPhone Number - ', Mike['tell'] )