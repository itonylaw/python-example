"""
File: ex21_matplot_02.py
Author: TonyDeep
Date: 2020-09-02
"""

import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62100]
ln1 = plt.plot(x_data, y_data, color = 'red', linewidth = 2.0, linestyle = '--')
ln2 = plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0, linestyle = '-.')
plt.title('TonyDeep.com', fontsize=20, fontname='Times New Roman')
plt.legend(labels=['Android', 'Java'], loc='lower right')
plt.show()