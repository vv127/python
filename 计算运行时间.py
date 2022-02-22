# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:36:07 2022

@author: vv123
"""
import time
import math
import numpy as np
x = np.arange(0, 100, 0.01)
t1 = time.process_time()
for i, t in enumerate(x):
    x[i] = math.pow(math.sin(t),2)
t2 = time.process_time()
print(t2 - t1)