import random
from link import Link
from neuro import Neuron


class Network:
    def __init__(self, *args):
        self.__nlayers = len(args)  # число шарів
        self.__neurons = args  # число нейронів у кожному шарі
        self.__layers = []  # нейрони у кожному шарі

        # створюємо нейрони у кожному шарі
        for i in range(self.__nlayers):
            self.__layers.append( [Neuron([], []) for n in range(self.__neurons[i])] )

        # створюємо зв\'язки між нейронами
        # повнозв\'язкова НМ (кожен нейрон із кожним нейроном)
        for i in range(self.__nlayers):
            for neuro in self.__layers[i]:  # перебір нейронів i-го шару
                # перший шар - нульовий, решта - із першого
                list_in = 0 if i == 0 else [Link(n_in, neuro, random.random()) for n_in in self.__layers[i - 1]]
                list_out = 0 if i == self.__nlayers - 1 else [Link(neuro, n_out, random.random()) for n_out in
                                                              self.__layers[i + 1]]
                neuro.list_in = list_in
                neuro.list_out = list_out

    def run(self, v):
        # подача сигналу на вхід НМ (вектор v)

        for neuro, inp in zip(self.__layers[0], v):
            neuro.value = neuro.list_in = inp

        # проводим сигнал по НМ
        for i in range(1, self.__nlayers):
            for neuro in self.__layers[i]:  # перебір i-го шару нейронів
                # вектор із добутків ваг нейронів на самі нейрони
                v = [(link.n_in.value * link.w) for link in neuro.list_in]
                # оброблення зваженої суми через сигмоїду
                neuro.value = neuro.act(sum(v))

    def output(self):
        # вивід значеннь нейронів вихідного шару
        return [neuro.value for neuro in self.__layers[-1]]
