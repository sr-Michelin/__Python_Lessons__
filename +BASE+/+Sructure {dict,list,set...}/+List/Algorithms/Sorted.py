import random


# задаєм тестовий список:
def func():
    return random.randint(-10, 10)


S = [func() for i in range(11)]
print(S)

# сортуємо його
N = len(S)
for i in range(N - 1):
    for j in range(i + 1, N):
        if S[i] > S[j]:
            S[i], S[j] = S[j], S[i]

print(S)
