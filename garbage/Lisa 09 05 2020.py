import math as m
import scipy.misc as sp
import random as rnd
from datetime import datetime
from joblib import Parallel, delayed
import multiprocessing

def nuton(f1, f2, x0, y0, eps=0.001, maxItr = 100):
    """f1(x, y) = 0,
       f2(x, y) = 0"""
    x = x0
    y = y0
    k = 0
    s = 100

    while k < maxItr and s > eps:

        a11 = sp.derivative(lambda x_: f1(x_, y), x)
        a12 = sp.derivative(lambda y_: f1(x, y_), y)
        a21 = sp.derivative(lambda x_: f2(x_, y), x)
        a22 = sp.derivative(lambda y_: f2(x, y_), y)

        det = a11*a22 - a12*a21
        if det == 0:
            print(f"Close because det = {det}!")
            return x, y, k, m.fabs(f1(x, y)) + m.fabs(f2(x, y))

        A11 = a22/det
        A12 = -a12/det
        A21 = -a21/det
        A22 = a11/det

        x_ = x - A11*f1(x, y) - A12*f2(x, y)
        y_ = y - A21*f1(x, y) - A22*f2(x, y)
        x = x_
        y = y_

        k = k + 1
        s = m.fabs(f1(x, y)) + m.fabs(f2(x, y))

    return x, y, k, m.fabs(f1(x, y)) + m.fabs(f2(x, y))


x, y, k, s = nuton(lambda x, y: 2*x - 4*y + 6, lambda x, y: 2*x + y - 4, 0, 0, 0.001, 15)

x, y, k, s = nuton(lambda x, y: x + y - 8, lambda x, y: 2*x*x + y*y - 82, -10, -10, 0.001, 15)

def nutonBIG(f1, f2, pairs, eps, maxItr = 100):
    return [nuton(f1, f2, x, y, eps, maxItr) for x, y in pairs]
    
    # result = []
    # for x, y in pairs:
    #     result.append(nuton(f1, f2, x, y, eps, maxItr))

    # return result


resultNutonBig = nutonBIG(lambda x, y: (x-1)*(y-2)*x*y, 
                          lambda x, y: (x+1)*(y-2)*m.sin(x), 
                          [(13, 15), (2, 3), (10, 32), (1,-3), (-2.3, 0.1), (9.1, 13), (10, -0.9), (1, 1),(10,1)], 
                          0.001, 150)
print ("\n".join(["abs = {} \t(x = {}, y = {}), \titr = {}".format(s, x, y, itr) for x, y, itr, s in resultNutonBig] ))



for x0, y0 in [(13, 15), (2, 3), (10, 32), (1,-3), (-2.3, 0.1), (9.1, 13), (10, -0.9), (1, 1),(-10,45),(45,79)]:
    x, y, k, sum = nuton(lambda x, y: (x-1)*(y-2)*m.cos(x), lambda x, y: (x+1)*m.exp(x), x0, y0, 0.001, 150)
    print ("x = " + str(x) + " y = "+ str(y) + " iter = " + str(k) + " sum = " + str(sum))




list1 = [(rnd.randrange(-20, 50), rnd.randrange(-20, 50)) for _ in range(1000)]
list2 = [(rnd.randrange(-20, 50), rnd.randrange(-20, 50)) for _ in range(1000)]
list3 = [(rnd.randrange(-20, 50), rnd.randrange(-20, 50)) for _ in range(1000)]



f1 = lambda x, y: (x-1)*(y-2)*x*y*m.cos(y)
f2 = lambda x, y: (x+1)*(y-2)*m.sin(x)


start_time = datetime.now()

nutonBIG( f1,  f2, list1, 0.001, 150)
nutonBIG( f1, f2, list2, 0.001, 150)
nutonBIG( f1,  f2, list3, 0.001, 150)

print("time = {}".format(datetime.now() - start_time))


list4 = [list1, list2, list3]

start_time = datetime.now()

Parallel(n_jobs=3)(delayed(nutonBIG)( f1,  f2, i, 0.001, 150) for i in list4)

print("timeParalel = {}".format(datetime.now() - start_time))




