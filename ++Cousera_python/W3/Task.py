import numpy as np
from math import sin, exp
import matplotlib.pylab as plt
from scipy.optimize import minimize, differential_evolution

# Task_1
print('\nTask_1')


def func1(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)


x_Arr1 = np.arange(1., 31.)  # задаємо проміжок по х
y_Arr1 = np.array([func1(x) for x in x_Arr1])  # задаємо проміжок по у через func1(х)

min_Fun1_val1 = minimize(func1, np.array(1))
print('При х = {0}, f(x) = {1} за {2} ітерацій.'.format(round(float(min_Fun1_val1.x), 3), round(min_Fun1_val1.fun, 3),
                                                        min_Fun1_val1.nit))
min_Fun1_val2 = minimize(func1, np.array(2), method='BFGS')
print('При х = {0}, f(x) = {1} за {2} ітерацій -- BFGS [x=2].'.format(round(float(min_Fun1_val2.x), 3),
                                                                      round(min_Fun1_val2.fun, 3),
                                                                      min_Fun1_val2.nit))
min_val_answer1 = np.zeros(2)
min_val_answer1[0] = round(min_Fun1_val2.fun, 2)

min_Fun1_val3 = minimize(func1, np.array(30), method='BFGS')
print('При х = {0}, f(x) = {1} за {2} ітерацій -- BFGS [x=30].'.format(round(float(min_Fun1_val3.x), 3),
                                                                       round(min_Fun1_val3.fun, 3),
                                                                       min_Fun1_val3.nit))
min_val_answer1[1] = round(min_Fun1_val3.fun, 2)
print(min_val_answer1)

with open('Task_1.txt', 'w') as val_answer1:
    for item in min_val_answer1:
        val_answer1.write(str(item) + ' ')

# Task_2
print('\nTask_2')
bounds = [(1, 30)]
min_Fun1_val4 = differential_evolution(func1, bounds)
print('При х = {0}, f(x) = {1} за {2} ітерацій -- Evolution [(1, 30)].'.format(round(float(min_Fun1_val4.x), 3),
                                                                               round(min_Fun1_val4.fun, 3),
                                                                               min_Fun1_val4.nit))
with open('Task_2.txt', 'w') as val_answer2:
    val_answer2.write(str(round(min_Fun1_val4.fun, 2)))

# Task_3
print('\nTask_3')


def func2(x):
    return int(func1(x))


x_Arr2 = np.arange(1., 31., 0.01)
y_Arr2 = np.array([func2(x) for x in x_Arr2])

min_Fun2_val1 = minimize(func2, np.array(30), method='BFGS')
print('При х = {0}, f(x) = {1} за {2} ітерацій -- BFGS [30].'.format(round(float(min_Fun2_val1.x), 3),
                                                                     round(min_Fun2_val1.fun, 3),
                                                                     min_Fun2_val1.nit))
min_val_answer2 = np.zeros(2)
min_val_answer2[0] = round(min_Fun2_val1.fun, 2)

min_Fun2_val2 = differential_evolution(func2, bounds)
print('При х = {0}, f(x) = {1} за {2} ітерацій -- Evolution [(1, 30)].'.format(round(float(min_Fun2_val2.x), 3),
                                                                               round(min_Fun2_val2.fun, 3),
                                                                               min_Fun2_val2.nit))
min_val_answer2[1] = round(min_Fun2_val2.fun, 2)
print(min_val_answer2)

plt.title('Comparison of different types in matplotlib')
plt.plot(x_Arr1, y_Arr1, label='float (original function)')
plt.plot(x_Arr2, y_Arr2, label='int')
plt.grid()
plt.legend()
plt.savefig('Comparison of different types in matplotlib')
plt.show()

with open('Task_3.txt', 'w') as val_answer3:
    for item in min_val_answer2:
        val_answer3.write(str(item) + ' ')
