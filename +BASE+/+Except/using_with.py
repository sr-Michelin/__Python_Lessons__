# Акуратний спосіб виведення строк
with open('using_with.txt', 'r') as f:
    for line in f:
        print(line, end='')
