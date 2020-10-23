# Програма переконується в тому, що файл закритий

import time

try:
    f = open('text.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)

except KeyboardInterrupt:
    print('!! Відміна читання файлу')

finally:
    f.close()
    print('\n(Очищення: закриття файла)')
