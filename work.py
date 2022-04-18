# -*- coding: utf-8 -*-

import numpy as np

A = np.arange(25).reshape(5,5)
A[[0,4],:] = A[[4,0],:]

print(A)














