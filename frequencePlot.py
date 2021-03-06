#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:28:05 2021

@author: lexipfalzgraf
"""
import matplotlib.pyplot as plt
import pandas as pd

HegelFreq=pd.read_csv('hegelFreq.csv')
MacyFreq=pd.read_csv('macyFreq.csv')
MontFreq=pd.read_csv('montFreq.csv')
WebFreq=pd.read_csv('webFreq.csv')
WilsonFreq=pd.read_csv('WilsonFreq.csv')


plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"
plt.locator_params(axis="x", nbins=13)
plt.locator_params(axis="y", nbins=6)
plt.xlabel("Year", loc='center')
plt.ylabel("Frequency of Usage by Author", loc='center')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(top=25)  
plt.ylim(bottom=0)

MacyFreq['Rolling'] = MacyFreq['Frequence'].rolling(5).mean()
MontFreq['Rolling'] = MontFreq['Frequence'].rolling(5).mean()
WebFreq['Rolling'] = WebFreq['Frequence'].rolling(5).mean()
WilsonFreq['Rolling'] = WilsonFreq['Frequence'].rolling(5).mean()
HegelFreq['Rolling'] = HegelFreq['Frequence'].rolling(5).mean()

HegelFreq['Rolling']= 100*HegelFreq['Rolling']
MacyFreq['Rolling']= 100*MacyFreq['Rolling']
MontFreq['Rolling']= 100*MontFreq['Rolling']
WebFreq['Rolling']= 100*WebFreq['Rolling']
WilsonFreq['Rolling']= 100*WilsonFreq['Rolling']

plt.plot(HegelFreq['Year'], HegelFreq['Rolling'], label = "Hegel", color="gainsboro",linewidth=1, linestyle="dashed")
plt.plot(MacyFreq['Year'], MacyFreq['Rolling'], label = "Macy", color="darkgrey",linewidth=1, linestyle="dotted")
plt.plot(MontFreq['Year'], MontFreq['Rolling'], label = "Montesquieu", color="dimgrey",linewidth=1, linestyle="dashdot")
plt.plot(WebFreq['Year'], WebFreq['Rolling'], label = "Weber", color="black",linewidth=1, linestyle="solid")
plt.plot(WilsonFreq['Year'], WilsonFreq['Rolling'], label = "Wilson", color="lightgrey",linewidth=1, linestyle="solid")


plt.legend(loc=1, prop={'size': 7})

#plt.savefig("freqAuthors.png",dpi=200, bbox_inches="tight")
plt.show()

