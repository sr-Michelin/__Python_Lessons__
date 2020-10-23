print('Програма, яка спонукає до вгадування задуманої раніш цифри.')

with open('guessing.txt', 'r') as f:
    for line in f:
        print()

running = True
num = int(line)  # num = 21
while running:
    try:
        num_predicted = int(input('Введіть число: '))
        if num_predicted > num:
            print('Введене число більше шуканого\n')
        elif num_predicted < num:
            print('Введене число менше шуканого\n')
        else:
            print('Вгадали!')
            running = False
    except ValueError:
        print('Ви ввели не число! \nTry again!\n')
