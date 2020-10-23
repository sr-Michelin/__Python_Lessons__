from math import *


def newton(f, Df, t0, epsilon, max_iter):
    tn = t0
    for n in range(1, max_iter + 1):
        ftn = f(tn)
        if abs(ftn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return tn
        Dftn = Df(tn)
        if Dftn == 0:
            print('Zero derivative. No solution found.')
            return None
        tn = tn - ftn / Dftn
    print('Exceeded maximum iterations. No solution found.')
    return None


f = lambda t: 2 ** t
Df = lambda t: 2 ** t * log(2)

approx = newton(f, Df, 1, 1e-10, 10000)
print('T = ', approx)
