import random
import time


def get_nod(a, b):
    """Алгоритм Евкліда для пошуку найбільшого спільного дільника"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod():
    """Просте тестування алгоритму Евкліда"""
    # -- тест 1 -----------------------------
    print('\nTest 1')
    a = 28
    b = 35
    res = get_nod(a, b)
    if res == 7:
        print('Перевірка пройшла успішно!')
    else:
        print('Помилка під час перевірки!')

    # -- тест 2 -----------------------------
    print('\nTest 2')
    a = 100
    b = 1
    res = get_nod(a, b)
    if res == 1:
        print('Перевірка пройшла успішно!')
    else:
        print('Помилка під час перевірки!')

    # -- тест 3 -----------------------------
    print('\nTest 3')
    a = 2
    b = 10000000
    st = time.time()
    res = get_nod(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print(f'Перевірка пройшла успішно!')
    else:
        print('Помилка під час перевірки!')

    # -- тест 4 -----------------------------
    print('\nTest 4')

    N = 0
    i = 1
    St = time.time()
    while dt < 1:
        A = [random.randint(1, N) for n in range(N)]
        B = [random.randint(1, N) for n in range(N)]

        st = time.time()
        rez = [get_nod(a, b) for a, b in zip(A, B)]
        et = time.time()

        dt = et - st


        N += 10000
        i += 1
    Et = time.time()
    DT = Et - St
    print(f'\nПеревірка пройшла успішно! \nЗагальний час {DT = }s')


if __name__ == '__main__':
    test_nod()

input()
