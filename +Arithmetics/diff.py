from sympy import *

x = symbols('x')

while True:
    f = input('\nВведіть формулу: ')
    df = diff(f)
    print('diff({0}) = {1}'.format(f, df))




