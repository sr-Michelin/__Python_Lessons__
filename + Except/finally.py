# Програма переконується в тому, що файл закритий

import  time as ti

try:
    f = open('text.txt')
    while True:
        line = f.readline()
        if  len (line) == 0:
            break
        print(line,end = '')
        ti.sleep(2)

except KeyboardInterrupt:
    print('!! Відміна читання файлу')

finally:
    f.close()
    print('\n(Очищення: закриття файла)')