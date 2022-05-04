#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:04:15 2022

@author: lexipfalzgraf
"""

import pandas as pd
import matplotlib.pyplot as plt

y_vals = [0.7310195228,0.1935483871,0.2186805041,0.2866141732,0.2200368777,0.1568361582,0.149537037,0.07066820572,0.07108118219,0.07069261591,0.04789311408]
x_vals = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]

y_vals = [y*100 for y in y_vals]


plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"
plt.xlabel("Year", loc='center')
plt.ylabel("Documents with 'Spirit' as a Percentage of Total", loc='center')
plt.ylim(top=100)  
plt.ylim(bottom=0)
plt.locator_params(nbins=11)
plt.xticks(x_vals)
plt.bar(x_vals,y_vals, width=4, color="grey")


#plt.savefig("spiritRatio.png",dpi=200, bbox_inches="tight")
plt.show()