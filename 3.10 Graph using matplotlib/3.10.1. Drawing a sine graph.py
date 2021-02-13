# 3.10.1 sin 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)    # [0, 0.1, 0.2, ... , 5.9]
y = np.sin(x)
plt.plot(x, y)
plt.show()