print("# Перцептрон")
print("")

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])
training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1  # Вага синапсів не може бути меншою, ніж -1 і більшою, аніж +1
print("Випадкові ваги:")
print(synaptic_weights)
print("")
n = int(input("Введіть кількість ітерацій: "))
# Метод зворотнього розповсюдження
for i in range(n):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weights += adjustment

print("")
print("Ваги після навчання:")
print(synaptic_weights)

print("")
print("Результат після навчання:")
print(outputs)

# TEST
new_inputs = np.array([1, 1, 0])  # нова ситуація
outputs = sigmoid(np.dot(new_inputs, synaptic_weights))

print("")
print("Нова ситуація:")
print(outputs)

input()
