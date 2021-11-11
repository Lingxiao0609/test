#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:03:12 2021

@author: zhanglingxiao
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.zeros((50,50))

"""
0:
1:
2:
3:
4:       
"""

arr[20:30,20:30] = 2

for i in range(50):
    for j in range(50):
        print(i,j)

"""
0: Susceptible
2: Infected
3: Removed /Dead
4: Resistent
"""


import numpy as np
import matplotlib.pyplot as plt



arr = np.zeros((50, 50))
arr[20:25, 20:25] = 2



for t in range(100):
    plt.matshow(arr, vmin=0, vmax=3)
    plt.colorbar()
    plt.savefig(f"test{t}.png")



for i in range(50):
    for j in range(50):



        change_i = np.random.randint(-1, 2)
        change_j = np.random.randint(-1, 2)

    ni = i + change_i
    nj = j + change_j



# periodic boundary conditions
ni = ni % 50
nj = nj % 50



agent = arr[i, j]
neighbor = arr[ni, nj]



# transition rules
if arr[i, j] == 0 and arr[ni, nj] == 2:
    arr[i, j] = 2



elif arr[i, j] == 2:
    arr[i, j] = np.random.choice([2, 3], p=[0.9, 0.1])



# plt.savefig("test.png")
        
        
        


