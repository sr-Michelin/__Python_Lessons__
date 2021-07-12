# модуль для зв\'язку між нейронами

class Link:
    def __init__(self, n_in, n_out, w=0):
        """посилання на вхідний нейрон, вихідний та на початкову вагу"""
        self.__in = n_in
        self.__out = n_out
        self.__w = w

    @property
    def n_in(self):
        return self.__in

    @property
    def n_out(self):
        return self.__out

    @property
    def w(self):
        return self.__w
