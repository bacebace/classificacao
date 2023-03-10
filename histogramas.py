# -*- coding: utf-8 -*-
"""histogramas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mq9SpY4G7Tl-un9J-Ocy_UvAMPB_ipo8

**Importar bibliotecas**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive

"""**Carregar dados**"""

drive.mount('/content/drive')

PATH='drive/My Drive/FLAI/01_classificacao/'
df=pd.read_csv(PATH+'base_prob.csv', sep=',')

df

plt.figure(figsize=(15,5))
plt.hist(df.age, bins= np.arange(0,101,1), rwidth=0.8)
plt.xticks(fontsize=15, ticks= np.arange(0,101,5))
plt.yticks(fontsize=15)
plt.xlabel('idade', fontsize=15)
plt.ylabel('quantidade de pessoas', fontsize=15)
plt.title('histograma: quantidade de pessoas vs idade', fontsize=15)
plt.grid();

plt.figure(figsize=(15,5))
plt.hist(df.age, bins= np.arange(0,101,1), rwidth=0.8, density=True)
plt.xticks(fontsize=15, ticks= np.arange(0,101,5))
plt.yticks(fontsize=15)
plt.xlabel('idade', fontsize=15)
plt.ylabel('probabilidade / idade', fontsize=15)
plt.title('histograma: probabilidade vs idade', fontsize=15)
plt.grid();

"""**Distribuição de probabilidade conjunta**"""

plt.figure(figsize=(15,5))
#plt.hist(df.age, bins= np.arange(0,101,1), rwidth=0.8, density=True)
plt.hist2d(df.age, df.MonthlyIncome, bins=30, density=True)
plt.xticks(fontsize=15, ticks= np.arange(0,101,5))
plt.yticks(fontsize=15)
plt.xlabel('idade', fontsize=15)
plt.ylabel('renda mensal', fontsize=15)
plt.title('distribuição de probabilidade conjunta (idade e renda mensal)', fontsize=15)
plt.colorbar();

plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
plt.hist(df.MonthlyIncome, bins=30, density=True, rwidth=0.8, orientation='horizontal')
#plt.title('renda mensal', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('probabilidade', fontsize=15)
plt.ylabel('renda mensal', fontsize=15)

plt.subplot(2,2,4)
plt.hist(df.age, bins=30, density=True, rwidth=0.8)
#plt.title('idade', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('idade', fontsize=15)
plt.ylabel('probabilidade', fontsize=15)

plt.subplot(2,2,2)
plt.hist2d(df.age, df.MonthlyIncome, bins=30, density=True)
plt.xticks(fontsize=15, ticks= np.arange(0,101,20))
plt.yticks(fontsize=15)
plt.xlabel('idade', fontsize=15)
plt.ylabel('renda mensal', fontsize=15)
plt.title('distribuição de probabilidade conjunta', fontsize=15)
plt.colorbar();