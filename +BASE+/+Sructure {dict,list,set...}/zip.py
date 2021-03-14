# У python функція zip() дозволяє пройтись одночасно по декільком ітеративним об\'єктам

A = [1, 2, 3]
B = ['a', 'b', 'c', 'e']

for i, j in zip(A, B):
    print(i, j)

print()

# -------------------
# видає кортеж елементів двох ітеративних об\'єктів, індекси яких співпадають
for i in zip(A, B):
    print(i, type(i))

print()

# -------------------
import itertools as iT

# Повноцінний прохід по всіх елементах (включає і ті, які за ідексом є остачею відносно двох об\'єктів --> None)
for i in iT.zip_longest(A, B):
    print(i)

print()

# -------------------
# fillvalue заповнює None потрібним знаком
for i in iT.zip_longest(A, B, fillvalue=4):
    print(i)

print()

# -------------------
ab = zip(A, B)
ab = list(ab)
print(ab)
print()

# -------------------
# Одночасний перехід по двох списках
names = ['Mike', 'Yara', 'Kolya', 'Sasha', 'Vanya']
scholarship = [1660, 1660, 1660, 0]

for i, j in iT.zip_longest(names, scholarship):
    print(f'{i} have a {j} UAN every month as scholarship')
print()

# -------------------
a = []
b = []

for i, j in zip(range(1, 10), range(10, 20)):
    a.append(i)
    b.append(j)
print(f'a = {a}, b = {b}')
