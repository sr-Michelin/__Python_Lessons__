# читання із файлу
try:
    file = open('Lucl.txt', 'r', encoding='utf-8')
    print(file.read())
    file.seek(0)  # зміна файлової позиції відносно початку файла
    print(f'{file.tell() = }')  # озвучує поточний номер файлової позиції
    print(file.readline())  # вивід одного рядка

    for line in file:  # ще один спосіб вивести вміст документа
        print(line, end='')
        pass

    file.seek(0)

    # для надійної роботи із файлами
    try:
        print(f'\n{file.readlines() = }')  # вивід цілого документа із знаками переносу у вигляді списку рядків
    finally:
        file.close()  # закриття файлу для оптимізації програми

except FileExistsError:
    print('Файл відсутній...')

# Найкращий спосіб роботи із файлами
with open('Lucl.txt', 'r', encoding='utf-8') as file:
    print('\nWith open():')
    for line in file:
        print(line, end='')

# запис у файл
# 'a+' - дозапис і читання
with open('open_out.txt', 'w', encoding='utf-8') as file:
    file.write('It\'s working!')

#