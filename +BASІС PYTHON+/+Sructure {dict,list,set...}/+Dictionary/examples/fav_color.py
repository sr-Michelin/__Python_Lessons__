fav_color = {
    'A': [1, 0, 1],
    'B': [2, 0, 2],
    'C': [3, 0, 3],
    'D': [4, 0, 4],
    'E': [5, 0, 5],
    'F': [6, 0, 6],
    'G': [7, 0, 7]
}
print('fav_color:', end='')
for name, colors in fav_color.items():
    print('\n', name, end=': ')
    for color in colors:
        print(color, end=' ')
