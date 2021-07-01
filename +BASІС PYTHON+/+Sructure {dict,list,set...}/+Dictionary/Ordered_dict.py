from collections import OrderedDict

my_dict = OrderedDict()
my_dict['A'] = [1, 0, 1]
my_dict['B'] = [2, 0, 2]
my_dict['C'] = [3, 0, 3]

for name, colors in my_dict.items():
    print('\n{}'.format(name),end=': ')
    for color in colors:
        print(color, end=' ')