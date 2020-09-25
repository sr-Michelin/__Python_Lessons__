while True:
    try:
        text = input('Введіть число: ')
        if text == 'stop':
            print('Стоп машина!')
            break
    except ValueError:
        print('Ви ввели не число!')
    else:
        print('Ви ввели число {0} без помилок'.format(text))

