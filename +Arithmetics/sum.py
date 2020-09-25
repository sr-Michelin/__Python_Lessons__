total = 0
count = 0

while True:
    l = input('Введіть будь-яке число: ')
    if l:
        try:
            num = int (l)
        except ValueError:
            print('Ви ввели не число!')
            continue
        except EOFError:
            break

        total += num
        count += 1

    else:
        break

    if count:
        mean = total/count
        print('count = {0}, total = {1}, mean = {2}'.format(count,total,mean))
