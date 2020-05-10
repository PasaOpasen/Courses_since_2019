# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:45:29 2020

@author: qtckp
"""


import numpy as np

s = int(input("Введите число секунд: "))

x = int(np.floor(s/60/60))

y = int(np.floor((s-x*60*60)/60))

z = int(np.floor(s - x*60*60 - y*60))

print(f"Всего {x} часов + {y} минут + {z} секунд")











