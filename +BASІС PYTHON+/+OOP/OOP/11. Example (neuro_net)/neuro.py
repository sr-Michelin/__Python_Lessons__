import math


class Neuron:
    def __init__(self, list_in, list_out):
        """Конструтор, який передає список вхідних та вихідних зв\'язків"""
        self.__in = list_in
        self.__out = list_out
        self.__value = 0  # яке вихідне значення має даний нейрон

    @property
    def list_in(self):
        return self.__in

    @list_in.setter
    def list_in(self, lst):
        self.__in = lst

    @property
    def list_out(self):
        return self.__out

    @list_out.setter
    def list_out(self, lst):
        self.__out = lst

    def act(self, x):
        """Сигмоїда"""
        return 1 / (1 + math.exp(-x))
