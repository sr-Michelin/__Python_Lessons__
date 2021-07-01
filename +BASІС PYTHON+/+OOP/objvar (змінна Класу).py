class Robot:
    population = 0

    def __init__(self, name):
        # Ініціалізація даних
        self.name = name
        print('\nІніціалізація {0}...'.format(self.name))

        # При створенні робот добавляється до змінної 'population'
        Robot.population += 1

    def __del__(self):
        # То є смерть
        print('{0} знищується!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} був останім'.format(self.name))
        else:
            print('Залишилося {0} робочих роботів/и...'.format(Robot.population))

    def say_HI(self):
        print('Вітаю! Мої хазяї називають мене {0}'.format(self.name))

    def how_many():
        print('У нас {0} роботів'.format(Robot.population))

    how_many = staticmethod(how_many)


droid1 = Robot('R2-D2')
droid1.say_HI()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_HI()
Robot.how_many()

droid3 = Robot('Chapie')
droid3.say_HI()
Robot.how_many()

droid4 = Robot('Ava')
droid4.say_HI()
Robot.how_many()

print('\nТут роботи виконуть роботу!')
print('\nРоботи виконали роботу. Утилізація...')
print('')

del droid1
del droid2
del droid3
del droid4

Robot.how_many()
