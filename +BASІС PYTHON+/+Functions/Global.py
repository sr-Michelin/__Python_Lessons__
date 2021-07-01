# nonlocal

A = 0


def fun(x):
    """Використання глобальної змінної А (метод global)"""
    global A
    A = 1
    print(f'{A**x = }')


def fun_out():
    """Зовнішня ф-ція"""
    A = 1

    def fun_in():
        """Внутрішня ф-ція"""
        nonlocal A  # зміна А=1 зовнішньої ф-ції на А=2 із внутрішньої (крок назовні)
        A = 2
        print(f'In {A = }')

    fun_in()
    print(f'Out {A = }')


print(f'Global {A = }')
fun(1)
fun_out()
