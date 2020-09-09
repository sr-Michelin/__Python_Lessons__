i = int (input("Введіть натуральне число: "))
def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
print("Факторіал: %s"% fact(i))


