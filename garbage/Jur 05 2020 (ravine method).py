# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:45:04 2020

@author: qtckp


the code is based on http://scask.ru/q_book_dig_m.php?id=98
http://kibevs.tusur.ru/sites/default/files/upload/work_progs/kes/mo_posobie.pdf
"""

from joblib import Parallel, delayed
import multiprocessing
import numpy as np



def make_step(f, begin, count_point=20, count_iter = 5, eps = 0.01):
    """Это функция, которая делает несколько шагов случайного спуска
    
    вокруг точки begin (в виде массива numpy) случайным образом выбирается count_point точек
    путём случаного смещения begin на 100eps% в обе стороны,
    из всех точек выбирается наилучшая, спуск повторяется count_iter раз    
    """
    
    res = begin.copy()
    mn = f(*res)
    
    for _ in range(count_iter):
        
        # случайные точки -- это лучшее решение *   1 + eps*(случайное число от -1 до 1) по каждой координате
        points = res*(1+(2*np.random.random_sample((count_point,res.size))-1)*eps)
        
        vals = np.array([f(*p) for p in points])
        
        if np.min(vals) < mn:
            mn = np.min(vals)
            #print(mn)
            res = points[np.argmin(vals)].copy()
    
    return res
   
    
def RavineDown(f, ro1, h=0.1, max_count = 15, count_point=20, count_iter = 5, eps = 0.01):
    """Метод овражного спуска
    
    аргументы: функция, начальное значение в виде массива numpy,
    шаг спуска, максимальное число итераций спуска и 3 параметра для метода случайного спуска
    
    функция прекращает работу, когда кончаются итерации или когда сходимость сильно замедлилась или прекратилась
    """
    
    print(f"Start result = {f(*ro1)} for arg = {ro1}")
    
    r1 = make_step(f, ro1, count_point, count_iter, eps)
    
    ro2 = ro1 + np.random.random_sample((ro1.size,)) # случайно отличается от ro1
    
    r2 = make_step(f, ro2, count_point, count_iter, eps)
    
    f1 = f(*r1)   
    f2 = f(*r2)
    
    k=0
    
    while k < max_count:
        ro2 = r2 + h*(r2 - r1)*np.sign(f1-f2)
        
        r1 = r2.copy()
        r2 = make_step(f, ro2, count_point, count_iter, eps)
        
        f1 = f2
        f2 =f(*r2)
                
        k+=1
        print(f"{k}) result = {f2}")
        
        if f1 - f2 < 0.000001: # если метод начал сходиться очень медленно или расходиться, прервать
            return r1.copy()
    
    return r2.copy()
    



# овражная функция    min = (8, 1)
    
f1 = lambda x,y: (x-8)**2 + (y-1)**2 +70*(y+(x-8)**2-1)**2+1; plot_function3D(f1)

f2 = lambda x,y: (x-8)**2 + (y-1)**2 +70*(y+x-9)**2+1; plot_function3D(f2)

f3 = lambda x,y: 70*(x-8)**2 + (y-1)**2 +1; plot_function3D(f3)

f4 = lambda x,y,z,q: 70*(x-8)**2 + (y-1)**2 +1+70*(z-8)**2 + (q-1)**2


# как использовать с numpy
f1(*np.array([1,2]))

make_step(f1,np.array([1,2]),20,5,0.01)


RavineDown(f1, np.array([1,2]), h=0.1, max_count = 250, count_point=20, count_iter =5, eps = 0.01)

RavineDown(f2, np.array([1,3]), h=0.2, max_count = 250, count_point=20, count_iter =5, eps = 0.01)

RavineDown(f3, np.array([2,5]), h=0.4, max_count = 250, count_point=20, count_iter =5, eps = 0.01)

RavineDown(f4, np.array([2,2,0,0]), h=0.5, max_count = 250, count_point=30, count_iter = 10, eps = 0.01)




# time https://blog.dominodatalab.com/simple-parallelization/

begins = [np.array(s) for s in [(1,2),(3,6),(0,0),(8,-1),(-1,-4)]]


%timeit [RavineDown(f1,b, h=0.1, max_count = 40, count_point=20, count_iter =5, eps = 0.01) for b in begins]

%timeit Parallel(n_jobs=3)(delayed(RavineDown)( f1,b, h=0.1, max_count = 40, count_point=20, count_iter =5, eps = 0.01) for b in begins)













