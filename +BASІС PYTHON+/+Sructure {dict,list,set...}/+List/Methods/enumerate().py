# "enumerate(iterable_obj)" -- на відміну від "range()" видає індекс елемента та його значення

def enumerate_(sequence, start=0):
    """Еквівалентний запис ф-ції enumerate(iterable_obj)"""
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


a = [1, 5, -5, 1, 3, -10, 2, 4]

print(f'old {a = } -- початковий список')

for i, x in enumerate(a):
    if x % 2 == 0:
        a[i] += 1

print(f'new {a = } -- заміна парних елементів на непарні ')

# отримуєм набір кортежів, що скадаються із номера ел-ту списку та його значення:
print(list(x for x in enumerate(a)), '-- через вбудовану ф-цію')
print(list(x for x in enumerate_(a)), '-- через функціональний запис')
