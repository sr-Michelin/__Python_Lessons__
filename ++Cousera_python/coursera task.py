def worry(x):
    try:
        queue[x - 2] = [1]
        print(queue, ', {}-й учасник почав хвилюватися'.format(x - 1))
    except IndexError:
        print('Недупостима операція із чергою!')


def calm(x):
    try:
        queue[x - 2] = [0]
        print(queue, ',{}-й учасник заспокоївся'.format(x - 1))
    except IndexError:
        print('Недупостима операція із чергою!')


def come(x):
    try:
        if x > 0:
            for x_ in range(x):
                queue.append([0])
        elif x < 0:
            for x_ in range(abs(x)):
                queue.pop(-1)
        print(queue, ', кількість людей в черзі: {} чоловік'.format(len(queue)))
    except IndexError:
        print('Черга пуста, вивід людей неможливий!')


def worry_count():
    print('Worry count:', queue.count([1]))


if __name__ == '__main__':
    flag = True
    print('Для завершення програми введіть будь-яке слово, яке не являється командою'.upper(),
          '\nСписок команд: worry x, calm x, come x, w_count, де x - ціле число')

    N = input('Введіть початкову кількість учачників черги: ')
    x = 0
    queue = []
    for m in range(int(N)):
        queue.append([0])

    while flag:
        com = input('Ведіть команду: ')
        if com.startswith('worry'):
            worry(int(com[5:]) + 1)
        elif com.startswith('calm'):
            calm(int(com[5:]) + 1)
        elif com.startswith('w_count'):
            worry_count()
        elif com.startswith('come'):
            come(int(com[5:]))
        else:
            print('Кінець програми...')
            flag = False

input()  # for .exe
