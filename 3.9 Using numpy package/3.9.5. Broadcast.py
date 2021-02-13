# 3.9.5. 브로드캐스트

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[1, 2],
              [3, 4]])
print(A + B)

B = np.array([[1, 2]])  # B = np.array([[1, 2], [3, 4]])
print(A + B)

B = np.array([[1],
              [2]])
print(A + B)

B = 2
print(A + B)
