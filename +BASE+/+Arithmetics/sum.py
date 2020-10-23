total = 0
i = 0

while True:
    l = input('Введіть будь-яке число: ')
    if l:
        try:
            num = int(l)
        except ValueError:
            print('Ви ввели не число!')
            continue
        except EOFError:
            break

        total += num
        i += 1

    else:
        break

    if i:
        mean = total / i
        print('iteration = {0}, total = {1}, mean = {2}'.format(i, total, mean))
