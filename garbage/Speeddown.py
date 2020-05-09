# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:59:18 2020

@author: qtckp
"""


import scipy.misc as sp
import scipy.optimize as opt
import math as m



def SpeedDown(f, x0, y0, eps=0.001, maxiter = 150):
    
    grad = lambda x, y: (sp.derivative(lambda x_: f(x_,y),x), sp.derivative(lambda y_: f(x,y_),y))
    
    g1, g2 = grad(x0,y0)
    
    k = 0
    
    while m.sqrt(g1*g1+g2*g2)>eps and k<maxiter:
                    
        minimized = lambda t: f(x0-t*g1,y0-t*g2)
        
        minimum = opt.minimize_scalar(minimized,bounds = (0,100), method='bounded')
        
        x0=x0-minimum.x*g1
        y0=y0-minimum.x*g2
        
        g1, g2 = grad(x0,y0)
        
        k+=1
    
    print('result = {}  x = {}  y = {}  count of iterations = {}  |gradient| = {}'.format(f(x0,y0),x0,y0,k,m.sqrt(g1*g1+g2*g2)))
    
    return x0, y0



SpeedDown(lambda x,y: x**2 + y**2, 100, 200)

SpeedDown(lambda x,y: (x-20)**2 + (y*y-2*y+1)**2, 100, 200)

# тут всякие вариации с функцией Растригина https://jenyay.net/Programming/ParticleSwarm

SpeedDown(lambda x,y: x**2 - m.cos(2*m.pi*x) + (y*y-2*y+1)**2, 100, 200)

SpeedDown(lambda x,y: x**2 - m.cos(2*m.pi*x) + (y*y-2*y+1) - m.cos(2*m.pi*y) , 10, 20)
SpeedDown(lambda x,y: x**2 - m.cos(2*m.pi*x) + (y*y-2*y+1) - m.cos(2*m.pi*y) , -10, 20)
SpeedDown(lambda x,y: x**2 - m.cos(2*m.pi*x) + (y*y-2*y+1) - m.cos(2*m.pi*y) , 100, -200)

# на функции Швеля не сходится
SpeedDown(lambda x,y: -x*m.sqrt(m.fabs(x))-y*m.sqrt(m.fabs(y)) , 1, -2)


def truepower(value, degree):
    if value >= 0:
        return value**degree
    return -m.fabs(value)**degree



SpeedDown(lambda x,y: x**5.5 + y**5.1, 100, 200) # dont work


# тут градиент = 0 значит скорее всего, что производные просто не нашлись

SpeedDown(lambda x,y: truepower(x,5.5) + truepower(y,5.1), 100, 200) # work but does not converge

SpeedDown(lambda x,y: truepower(x,5.5) + truepower(y,5.1), 10, 20) # work but does not converge


#
# метод не всегда сходится
# но он и не обязан
#
#


# это функция принимает формулу на питоне и делает с ней спуск
def StringSpeedDown(formula, x0, y0, eps=0.001, maxiter = 150):
    return SpeedDown(lambda x,y: eval(formula), x0, y0, eps, maxiter)

StringSpeedDown('x**2+y**2',1,1)





import numpy as np

def der(g, r, eps = 0.00001):
    right = (g(r+eps)-g(r))/eps
    left = (-g(r-eps)+g(r))/eps
    res = not np.isclose(right,left,atol=0.001)
    if res:
        print('right = {}  left = {}     eps = {}'.format(right,left,eps))
    return res


def SpeedDown2(f, x0, y0, eps=0.001, maxiter = 150):
    
    grad = lambda x, y: (sp.derivative(lambda x_: f(x_,y),x), 
                         sp.derivative(lambda y_: f(x,y_),y),
                         der(lambda x_: f(x_,y),x,eps/100),
                         der(lambda y_: f(x,y_),y,eps/100)      )
    
    g1, g2, t1, t2 = grad(x0,y0)
    
    if t1 or t2:
        return 'derivative does not exist  iter = {}'.format(0)
    
    k = 0
    
    while m.sqrt(g1*g1+g2*g2)>eps and k<maxiter:
                    
        minimized = lambda t: f(x0-t*g1,y0-t*g2)
        
        minimum = opt.minimize_scalar(minimized,bounds = (0,100), method='bounded')
        
        x0=x0-minimum.x*g1
        y0=y0-minimum.x*g2
        
        g1, g2, t1, t2 = grad(x0,y0)
        
        if t1 or t2:
            return 'derivative does not exist  iter = {}'.format(k+1)
        
        k+=1
    
    print('result = {}  x = {}  y = {}  count of iterations = {}  |gradient| = {}'.format(f(x0,y0),x0,y0,k,m.sqrt(g1*g1+g2*g2)))
    
    return x0, y0


SpeedDown2(lambda x,y: x**2 + y**2, 100, 200)

SpeedDown2(lambda x,y: truepower(x,5.5) + truepower(y,5.1), 10, 20) # work but does not converge




























