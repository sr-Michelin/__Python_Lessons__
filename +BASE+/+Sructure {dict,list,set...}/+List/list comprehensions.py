# Створення генераторів списків

A = [x for x in range(11) if x % 2 == 0]
print(A)

B = ['Mike', 'Kolya', 'Ivan', 'Sasha', 'Taras', 'Yra', 'Yaryna']
print(', '.join([name for name in B if len(name) == 4]))