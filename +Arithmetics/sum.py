count = 0
total = 0

while True:
    l = input('Введіть число: ')
    if l:
        try:
            num = int(l)
        except ValueError as err:
            print(err)
            continue

        total +=num
        count +=1
    else:
        break
    if count:
        mean = count/total
        print('count = {0}, total = {1}, mean = {2}'.format(count,total,mean))