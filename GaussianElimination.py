'''
Systems of Linear Algebraic Equations
Gaussian Elimination Method 
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''
import numpy as np

A = np.array([[60, 91, 26], [60, 3, 75], [45, 90, 31]], dtype='float')
b = np.array([1, 0, 0])

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(b)

for i in range(n):
    a = Ab[i]

    for j in range(i + 1, n):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

for i in range(n - 1, -1, -1):
    Ab[i] = Ab[i] / Ab[i, i]
    a = Ab[i]

    for j in range(i - 1, -1, -1):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

x = Ab[:, 3]

print(x)
