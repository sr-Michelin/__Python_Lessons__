# Ітератор

def sq(x):
    return x ** 2


lst = [i for i in range(11)]
M = map(sq, lst)

for i in lst:
    print(next(M), end=' ')

# ----------------------------------------
print('\r')
lst_1 = ['Львів', 'Київ', 'Харків', 'Одеса', 'Кривий ріг', 'Луганськ']
b = list(map(len, lst_1))
print(b)
