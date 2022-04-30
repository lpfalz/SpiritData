#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:23:27 2021

@author: lexipfalzgraf
"""

import pandas as pd
import matplotlib.pyplot as plt
import jsonlines


df= pd.DataFrame(columns=["creator","datePublished","docType","fullText","id","identifier","isPartOf","issueNumber","language","outputFormat","pageCount","pageEnd","pageStart","pagination","provider","publicationYear","publisher","sourceCategory","tdmCategory","title","url","volumeNumber","wordCount"])
i=0  
with jsonlines.open('spirit.jsonl') as f:
    for line in f.iter():
        df.loc[i]=(line)
        i+=1

df.drop(df[df['publicationYear']>2015].index, inplace=True)
y_vals = df['publicationYear'].value_counts().sort_index()
df=df.drop_duplicates(subset=['publicationYear'], keep='first')
timeV=pd.to_datetime(df['datePublished'])
yearT=timeV.dt.year.sort_values()
yearCount= pd.DataFrame(index=yearT,data=y_vals)

plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"

yearCount['Rolling'] = yearCount['publicationYear'].rolling(5).mean()

plt.locator_params(nbins=13)

plt.bar(yearT,yearCount['publicationYear'], align='center',width=1,edgecolor="dimgrey",color=(0,0,0,.3))

plt.xlabel("Publication Year", loc='center')
plt.ylabel("Number of Documents", loc='center')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.plot(yearCount['Rolling'], label='Simple Moving Average',linewidth=1, color='black')
plt.legend(loc=2, prop={'size': 9})

plt.savefig("task1.png",dpi=200, bbox_inches="tight")

