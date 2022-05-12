#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:15:52 2021

@author: lexipfalzgraf
"""
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"

#add ['author', count] tuple to list to add it to graph
author_count=[['Aristotle', 18],['Pye',52],['Diamond',74],['Ruggiero', 135],['Wilson',309],['Beard', 161],['Weber',232],['Hegel',299],['Macy',382],['Montesquieu',675]]
sorted_count=sorted(author_count, key=lambda x: x[1])

category=[x[0] for x in sorted_count]
counts=[x[1] for x in sorted_count]

fig, ax = plt.subplots()
p1=plt.barh(category,counts,color="gray",edgecolor="black")
plt.bar_label(p1,padding=3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig("countsNoReligion.png",dpi=200, bbox_inches="tight")
plt.show()
