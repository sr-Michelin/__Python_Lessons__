# тут ми проходимося по кортежу *contain
def make_juice(volume, *contain):
    print('We have a {0}L of juice, wich contain:'.format(volume), end=' ')
    for i in contain:
        print(i, end=' ')


make_juice(10, 'orrange', 'aplle')