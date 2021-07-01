import time


# Для використання запису декоратора у вигляді @func ф-цію обгортки піднімають над цільовою ф-цією

def time_test(fn):
    """Визначення часу, потраченого на виконання буль-якої ф-ції (при *args, **kwargs)"""

    def wrapper(*args, **kwargs):
        st = time.time()
        fn(*args, **kwargs)
        dt = time.time() - st
        print(f'Час роботи функції - {dt} s')

    return wrapper


def get_nod(a, b):
    """НДС двох цілих чисел"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def fast_get_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


print('----Перший спосіб (повільний):')
test_1 = time_test(get_nod)  # перший спосіб
test_1(100000000, 2)

print('----Перший спосіб (швидкий):')
test_2 = time_test(fast_get_nod)
test_2(100000000, 2)


# Або:
def time_test(fn, *args, **kwargs):
    """Визначення часу, потраченого на виконання буль-якої ф-ції (при *args, **kwargs)
    Менш гнучкий спосіб"""
    st = time.time()
    fn(*args)
    dt = time.time() - st
    print(f'Час роботи функції - {dt} s')


print('\n----Другий спосіб (повільний):')
time_test(get_nod, 100000000, 2)

# Використання способу "@":
print('\n----Спосіб 3 (через "@"):')


def time_test(fn):
    """Визначення часу, потраченого на виконання буль-якої ф-ції (при *args, **kwargs)"""

    def wrapper(*args, **kwargs):
        st = time.time()
        fn(*args, **kwargs)
        dt = time.time() - st
        print(f'Час роботи функції - {dt} s')

    return wrapper


@time_test
def get_nod(a, b):
    """НДС двох цілих чисел"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


get_nod(100000000, 2)
