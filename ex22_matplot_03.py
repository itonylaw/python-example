"""
File: ex22_matplot_03.py
Author: TonyDeep
Date: 2020-09-02
"""

import matplotlib.pyplot as plt
import numpy as np

# data = np.random.randint(0, 1000, 1000)
data = np.random.randn(1000)
plt.hist(data, bins=40, facecolor = 'blue', edgecolor = 'black', alpha = 0.7)
plt.show()
