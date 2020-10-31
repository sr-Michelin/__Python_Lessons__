from numpy import fabs

print('Програма, яка спонукає до вгадування задуманої раніш цифри.')

with open('guessing.txt', 'r') as f:
    for line in f:
        print()

running = True
num = int(line)  # num = 21
while running:
    try:
        num_predicted = int(input('Введіть число: '))
        if num_predicted == num:
            print('Вгадали!')
            running = False
        else:
            print('Введене число відрізняється задуманого на {0} років(и).'.format(int(fabs(num_predicted - num))))

    except ValueError:
        print('Ви ввели не число! \nTry again!')

    finally:
        print('Блок finally\n')
