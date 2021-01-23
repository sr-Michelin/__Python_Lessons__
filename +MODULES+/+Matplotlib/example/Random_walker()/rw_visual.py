import sys
import matplotlib.pyplot as plt

sys.path.append('E:\\DOCK\\Python_M\\vеnv\\+LESSONS\\+MODULES+\\+Matplotlib\\example\\Random_walker()')
from random_walk import Random_walk

# Безкінечна побудова б/р
while True:
    rw = Random_walk()
    rw.fill_walk()

    plt.style.use('classic')

    # Виведення точок в порядку зростання за допомогою градієнта кольлорів:
    point_num = range(rw.num_points)
    plt.scatter(rw.x_val, rw.y_val, c=point_num, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Виділення першої і останьої точки:
    plt.scatter(0, 0, c='green', edgecolors='none', s=40)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=40)
    plt.show()

    # Видалення осей (для красоти):
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    running = input('Make another walk? (y/n): ')
    if running != 'y':
        print('End of the program..')
        break
