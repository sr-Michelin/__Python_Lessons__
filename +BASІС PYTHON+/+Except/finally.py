# Програма переконується в тому, що файл закритий

import time

line = [' ']
f = line

try:
    f = open('using_with.txt')
    while len(line) > 0:
        line = f.readline()
        print(line, end='')
        time.sleep(0.5)

except KeyboardInterrupt:
    print('!! Відміна читання файлу')

finally:
    f.close()  # у будь-якому випадку
    print('\n(Очищення: закриття файла)')
