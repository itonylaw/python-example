"""
File: ex20_numpy.py
Author: TonyDeep
Date: 2020-09-02
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2.5, 0.1)
y1 = np.sin(np.pi * t)
y2 = np.sin(np.pi * t + np.pi / 2)
y3 = np.sin(np.pi * t - np.pi / 2)
plt.title('TonyDeep.com')
plt.plot(t, y1, 'b--', t, y2, 'g', t, y3, 'r-.')
plt.show()
