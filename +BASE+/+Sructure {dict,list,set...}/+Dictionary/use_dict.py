
Mike = {'first name' :'Mike',
        'middle name':'*******',
        'last name'  :'********',
        'adress'     : ['м.*****','вул.********','буд.*****','к.*****'],
        'tell'       : '************'}

print('Adress of Mike - ',Mike['adress'])

del Mike['tell']

print('\nNEW number of keys - {0} '.format(len(Mike)))   # Кількість ключів

for key,name in Mike.items():
    print('Key {0} with meaning {1}'.format(key,name))   # Запис ключів із їх значеннями

Mike['tell'] = '*********'
if 'tell' in Mike:
    print('\nPhone Number - ', Mike['tell'] )