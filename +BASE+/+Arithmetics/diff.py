from sympy import *


t = symbols('t')

while True:
    f = input('\nВведіть формулу: ')
    f = 2**t
    df = diff(f)
    print('diff({0}) = {1}'.format(f, df))
