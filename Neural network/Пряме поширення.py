import numpy as np


def act(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    """Функція, що задає логіку примітивної нейронки на побутовому прикладі вибору партнера"""
    x = np.array([house, rock, attr])

    w11 = [0.3, 0.3, 0]  # ваги для першого нейрона
    w12 = [0.4, -0.5, 1]  # ваги для другого нейрона

    weight_1 = np.array([w11, w12])  # матриця 2х3 {два нейрони прихованого шару із трьома вхідними з'язками}
    weight_2 = np.array([-1, 1])  # вектор 1х2 {вектор звязку для вихідного шару}

    sum_hidden = np.dot(weight_1, x)  # сума на вхід прихованого шару
    print('Значення суми на нейронах прихованого шару: {}'.format(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('Значення суми на виходах нейронів прихованого шару: {}'.format(out_hidden))

    sum_end = np.dot(weight_2, out_hidden)
    y = act(sum_end)
    print('Вихідне значення нейронки: {}'.format(y))

    return y


house = 1  # присутність власної квартири
rock = 0  # (музичні) уподобання/хобі, які не підходять нашій корисливій подрузі
attr = 1  # фізіологічна привабливість

res = go(house, rock, attr)

if res == 1:
    print('\nВона каже "Так"!')
else:
    print('\nФрензона...')