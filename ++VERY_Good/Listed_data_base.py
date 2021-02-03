class units:
    def __init__(self, volume, price, quality):
        self.volume = volume
        self.price = price
        self.quality = quality


class present_js(units):
    def __init__(self, origin, volume, price, quality):
        # units.__init__(self, volume, price, quality)
        super().__init__(volume, price, quality)
        print('We have {0} juice with volume {1}L, price {2} UAN ans quality {3}%'.format(origin, volume,
                                                                                          price, quality))


# Js_ = [present_js('Apple', 10, 19, 59), present_js('Orange', 5, 25, 91), present_js('Blueberry', 1, 38, 99)]
Js_ = []
run = 1
a = 1
while run:
    A = input('\nCreate new juice (y/n)? ')

    if A == 'y':
        print('Juice {}: '.format(a))
        a += 1
        Js_.append(
            present_js(input('\tOrigin: '), float(input('\tvolume: ')), float(input('\tprice: ')),
                       float(input('\tquality: '))))
    else:
        run = 0


def average():
    sum_vol = 0
    sum_price = 0
    sum_quality = 0

    if len(Js_) > 0:
        print('Let\'s go to average\'s')
        for n in range(0, len(Js_)):
            sum_vol += Js_[n].volume
            sum_price += Js_[n].price
            sum_quality += Js_[n].quality

        print('_' * 80, '\nAverages of {0} different juices: '
                        'volume - {1}L, price - {2} UAN, quality - {3}%'.
              format(len(Js_), round(sum_vol / len(Js_), 2), round(sum_price / len(Js_), 2),
                     round(sum_quality / len(Js_), 2)), '\n{}'.format('_' * 80))
    else:
        print('List of juices is empty..')


if __name__ == '__main__':
    average()

input()
