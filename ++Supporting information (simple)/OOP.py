class default():
    def __init__(self, vol):
        self.vol = vol


class Js_(default):
    def __init__(self, vol):
        # default.__init__(self, vol)
        super().__init__(vol)
        print('Volume of chosen juice: ', vol)


Orange = Js_(10)
Apple = Js_(12)
Man = Js_(10)


def sum():
    print('Common volume of chosen juices - {}'.format(Orange.vol + Apple.vol + Man.vol))


if __name__ == '__main__':
    sum()
