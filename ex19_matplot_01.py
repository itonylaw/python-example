"""
File: ex17_matplot_01.py
Author: TonyDeep
Date: 2020-09-02
"""

import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.show()

plt.axis([0, 5, 0, 20])
plt.title('TonyDeep.com', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color = 'gray')
plt.ylabel('Square values', color = 'gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y=x^2', fontsize=20)
plt.grid(True, linestyle='--', alpha=0.5)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()

