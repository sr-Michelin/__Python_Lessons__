# Cуть superполягає в тому, щоб не уникати написання батьківського класу.
# Суть полягає в тому, щоб викликати наступний метод у рядку в порядку роздільної здатності методу (MRO).
# Це стає важливим при багаторазовому успадкуванні.

# super(self.__class__, self).__init__()  # DON'T DO THIS! EVER.

class main:
    def __init__(self):
        print('main.__init__(self) - батьківський клас')


class inh_0(main):
    def __init__(self):
        # main.__init__(self) - явне наслідування (привіт багам і глічам)
        super().__init__()  # неявне наслідування (більш 'культурний' метод)
        print('inh_0.__ linit__(self) - наслідування із main')


class inh_1(main):
    def __init__(self):
        super().__init__()
        print('inh_1.__ linit__(self) - наслідування із main')


class inh_2(main):
    def __init__(self):
        super().__init__()
        print('inh_2.__ linit__(self) - наслідування із main')


class inh_3_all(inh_2, inh_1, inh_0):
    """\nDiamond structure (ромб, який починається із головного класу, продовжується дочірними,
і закінчується узагальненням дочірних)"""

    def __init__(self):
        super().__init__()
        print('inh_3.__ linit__(self) - узагальнення дочірних підкласів')


class inh_all(inh_3_all):
    """All"""

    def __init__(self):
        super().__init__()
        print('All')


J = inh_all()
print(inh_3_all.__doc__)
print(inh_3_all.mro())
