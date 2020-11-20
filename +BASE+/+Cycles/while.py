# Угадайка на циклах
import time
a = time.localtime().tm_year - 1998

running = True

while running:
    try:
        ques = int(input('Введіть ціле число: '))
        if ques == a:
            print('Ви вгадали!')
            running = False
        elif ques < a:
            print('Введене чило менше загаданого.')
        else:
            print('Введене чило більше загаданого.')
    except ValueError:
        print('Ви ввели не число!')
else:
    print('Цикл завершений...')
i = input()
