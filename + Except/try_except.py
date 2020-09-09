try:
    text = input('Введіть число:')
except ValueError:
    print('Ви ввели не число!')
else:
    print('Ви ввели число {0} без помилок'.format(text))