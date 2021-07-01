import random

A = [random.randint(-10, 10) for x in range(10)]  # задаємо тестову вибірку
B = sorted(A, reverse=False)
C = A.sort(reverse=True)

print(f'RAW {A = }')


# Сортування за правилом: спочатку парні, потім непрарні цифри
def func_sort(x):
    return x % 2


print(sorted(A, key=func_sort), ' -- класичний спосіб')
print(sorted(A, key=lambda x: x % 2), ' -- lambda - спосіб')

# сортування за довжиною елементів списку
S = ['Київ', 'Одеса', 'Харків', 'Львів', 'Кристинопіль']
print(sorted(S, key=len), ' -- сортування за довжиною строки (міста)')

# сортування за першим/останім символом
print(sorted(S, key=lambda x: x[0]))

# сортування за певним ключем
students = {
    ('Mike Shevchenko', 6, 5, 1660),
    ('Kolya Husev', 6, 0, None),
    ('Yaryna Ostapchuk', 6, 7, 1660),
    ('Ivan Golubosh', None, 0, None),
    ('Victor Poverjuk', 6, 2, 2200),
    ('Sviatoslava Andruhovych', 6, 1, 2200)
}
print(f'{list(sorted(students, key=lambda x: x[2])[i][0] for i in range(len(students)))} -- сортування за рейтингом')
