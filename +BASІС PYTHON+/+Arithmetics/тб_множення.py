n = 1
for i in range(0, 10):
    for j in range(0, n * 11, n):
        print(j, end=' ')
    print()
    n += 1