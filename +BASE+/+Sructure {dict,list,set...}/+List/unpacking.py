first, *middle, last = 'Mike', 'Segiyovich', 'Shevchenko'
print(last)


# ---------------------------------------------

def sum_(x, y, z):
    rez = x + y + z
    print(f'X + Y + Z = {rez}')
    return rez


source = [1, 1, 1]
sum_(*source)
sum_(3, *source[1:])

