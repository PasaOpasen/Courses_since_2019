import math as m
import numpy as np

k = 2


def decision(f, u, X = 1, T = 1, xCount = 10, tCount = 100):
    hh = X/xCount
    t = T/tCount
    coef=t/hh**2

    ix = np.zeros(xCount+1)
    iy = np.zeros(xCount+1)

    for i in range(xCount + 1):
        ix[i] = u(0, i * hh)

    for i in range(tCount):
        iy[0] = u(i * t, 0)

        for j in range(1, xCount):
            iy[j] = ix[j] + coef * (ix[j + 1] - 2 * ix[j] + ix[j - 1]) + t * f(i * t, j * hh)

        iy[xCount] = u(i * t, X)
        
        for j in range(xCount + 1):
            ix[j] = iy[j]
            
    eps = m.fabs(iy[xCount] - u(T, X))
    print("pred = {}   actual = {}  eps = {}".format(iy[xCount], u(T, X), eps))


decision(
    lambda t, x: m.sin(k * x) * (1 + k * k * (-1 + t))+1, 
    lambda t, x: (t - 1) * m.sin(x * k)+t, 
    2, 3, 10, 100)