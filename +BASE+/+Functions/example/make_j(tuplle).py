# тут ми проходимося по кортежу *contain
def make_juice(volume, *contain):
    print(f'We have a {volume}L of juice, which contain:', end=' ')
    for i in contain:
        print(i, end=' ')


make_juice(10, 'orange', 'apple')
