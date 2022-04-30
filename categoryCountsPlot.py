#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:15:52 2021

@author: lexipfalzgraf
"""
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"

category=['Aristotle','Pye','Diamond','Ruggiero','Wilson','Beard','Weber','Hegel','Macy','Montesquieu']

counts=[18,52,74,135,136,161,232,315,338,602]

fig, ax = plt.subplots()

p1=plt.barh(category,counts,color="gray",edgecolor="black")

plt.bar_label(p1,padding=3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig("countsNoReligion.png",dpi=200, bbox_inches="tight")
plt.show()
