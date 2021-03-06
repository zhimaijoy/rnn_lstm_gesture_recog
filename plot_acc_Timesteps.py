#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:54:21 2017

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


x_1 = [-30,-20, -15,  -10, -5, -2, -1]
accuracy_1 = [20.833, 44.167, 50.833, 95.833, 100, 100, 100]

x=np.array(x_1)
accuracy = np.array(accuracy_1)

fig, ax = plt.subplots(1,1)
axis_font = {'fontname':'Arial', 'size':'50'}

p1, =plt.plot( x, accuracy, label="Batch Size=2 Hidden Layers = 1 Hidden Cells = 512 Iterations= 1000", linewidth=5, marker='o', markeredgewidth= '5', markerfacecolor='black', color='b')
#for xy in zip(x, accuracy):                                       
#    ax.annotate('(%s, %s)' % xy, fontsize = 35, xy=xy, textcoords='data')

ax.text(-35, 50, 'Data Points \n (-30, 20.833) \n (-20, 44.167) \n (-15, 50.833) \n (-10, 95.833) \n (-5, 100) \n (-2, 100) \n (-1, 100)', style='italic', fontsize = 35,
        bbox={'facecolor':'red', 'alpha':3.5, 'pad':10})

# major ticks every 20, minor ticks every 5                                      
major_ticks = np.arange(0, 101, 5)                                              
minor_ticks = np.arange(-101, 101, 1)                                               

ax.set_xticks(major_ticks)                                                       
ax.set_xticks(minor_ticks, minor=True)                                           
ax.set_yticks(major_ticks)                                                       
ax.set_yticks(minor_ticks, minor=True)                                           

# and a corresponding grid                                                       

ax.grid(which='both') 

plt.ylim([0,120])
plt.xlim([-40,0])
plt.xlabel('Evaluation at time steps', **axis_font)
plt.ylabel('Accuracy of Prediction', **axis_font)

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

gridlines = ax.get_xgridlines() + ax.get_ygridlines()

#for line in gridlines:
 #   line.set_linestyle()

ax.xaxis.set_tick_params(labelsize=30)
ax.yaxis.set_tick_params(labelsize=30)

plt.legend([p1], loc='upper center', fontsize = 25, borderaxespad=0.)	#
plt.show()
#fig.savefig('figure.png')
