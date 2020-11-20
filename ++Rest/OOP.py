class default():
    def __init__(self, vol):
        self.vol = vol

class Js_(default):
    def __init__(self, vol):
        default.__init__(self, vol)
        print('Volume of choosen juice: ', vol)

Orange = Js_(10)
Aple = Js_(12)
Man = Js_(999)

def sum():
    print('Common volume of choosen juices - {}'.format(Orange.vol + Aple.vol + Man.vol))


if __name__ == '__main__':
    sum()
