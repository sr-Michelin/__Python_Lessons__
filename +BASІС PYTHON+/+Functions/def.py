"""---------------Фунції---def-add-return--------lambda-------------------------------------"""


def f(x, y, z):
    return (x ** 2) + (y ** 2) + (z ** 2)


print(f(2, 2, 2))
"--------------------------------"


# Калькулятор трохи
def func(x):
    def add(y):  # додає(У)
        return x + y  # ф-ла (1)

    return add


t1 = int(input("X: "))
test = func(t1)
t2 = int(input("Y: "))
print("X+Y=", test(t2))  # підставляє введені значення х та у у формулу (1)
"--------------------------------"


def f():
    pass  # функція нічого не повертає


print(f())
"--------------------------------"


def f(x, y, a=5):  # (x+y)^a
    res = x + y
    res **= a
    return res


print("(x+y)^a=", f(int(input("X: ")), int(input("Y: "), )))
"--------------------------------"


def f2(*args):  # *коли не вказано кількіть змінних - КОРТЕЖ
    return args


print(f2(1, 2, 3))
"--------------------------------"


def f3(**args2):  # **словник
    return args2


print(f3(short='dict', longer="dictionary"))
"--------------------------------"


def f4(**args3):
    return args3


print(f4(short='dict', longer="dictionary"))

# анонімні функції
add = lambda x, y: x * y
"--------------------------------"
print(add(2, 5))  # запис через lambda - без return
print((lambda x, y: x * y)(2, 6))  # ще один запис через lambda (коротший)
"--------------------------------"
fun = lambda *args: args  # ще один запис через lambda
print(fun(1, 2, 3))

"--------------------------------"
A = [x for x in range(11) if x % 2 == 0 and x >= 6]
B = (lambda x: x)(A)
print(B)
