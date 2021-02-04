from random import choice


class Random_walk:
    """Генерація випадкового блукання - броунівського руху """

    def __init__(self, num_points=50000):
        self.num_points = num_points
        # Блукання починаються з точки (0,0)
        # створення двох списків для збереження координат:
        self.x_val = [0]
        self.y_val = [0]

    def fill_walk(self):
        """Обчислення усіх точок блукааня"""

        # Генерація кроків до досягнення потрібної довжини
        while len(self.x_val) < self.num_points:
            # Визначення напрямку і довжини переміщення:
            x_dir = choice([1, -1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist

            y_dir = choice([1, -1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dist

            # Відмова від нульових переміщень:
            if x_step == 0 and y_step == 0:
                continue

            # Обчислення наступних значень x,y:
            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step

            self.x_val.append(x)
            self.y_val.append(y)
