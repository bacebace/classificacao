# -*- coding: utf-8 -*-
"""naive_bayes_gaussian.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YBFuDKiWlRS1gHz_Llqxc-SQ4pQniUn2

##Importar bibliotecas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import norm

from sklearn.naive_bayes import GaussianNB

from google.colab import drive

drive.mount('/content/drive')

PATH='drive/My Drive/FLAI/01_classificacao/'
df=pd.read_csv(PATH+'base_gaussiannb.csv', sep=',')

df

"""##Revisão: naive bayes

$P(Y|idade) = \frac{P(idade|Y) * P(Y)}{P(idade)}$

Qual a probabilidade de Y=1 (cliente fazer o depósito) dada a idade (idade=30, por exemplo)?

* Calcular P(Y) é fácil;
* P(idade) não precisa ser calculada, pois podemos normalizar com:

$P(Y=0|idade) + P(Y=1|idade) = 1$

* Estimar P(idade|Y) é **difícil**, pois há muito ruído.

Lembre-se também que normalmente existem muitas variáveis!

## Hipótese extra no gaussian naive bayes

Hipótese: a distribuição de $P(idade|Y)$ é uma **distribuição normal**.

O histograma é aproximado por uma distribuição normal, como veremos no gráfico a seguir.

Não será uma aproximação que realmente mostra a probabilidade exata, pois a distribuição verdadeira não é uma normal, porém a **ordenação** é boa. É o conceito de *score*: geram-se *scores* maiores para clientes mais propensos a fazer o depósito.
"""

media = df.loc[df.y==1].age.mean() # média da idade de quem deposita
std = df.loc[df.y==1].age.std() # desvio padrão de idade de quem deposita

plt.figure(figsize=(15,5))
plt.hist(df.loc[df.y==1].age, rwidth=.8, bins=np.linspace(0,100,100), color='r', alpha=.3, density=True)
plt.title("Fez o depósito")

x=np.linspace(0,100,300)
plt.plot(x, norm.pdf(x,media,std),'r-');
#pdf é distribuição de densidade de probabilidade
#criada a partir da média e do desvio padrão

media_n = df.loc[df.y==0].age.mean() # média da idade de quem não deposita
std_n = df.loc[df.y==0].age.std() # desvio padrão de idade de quem não deposita

plt.figure(figsize=(15,5))
plt.hist(df.loc[df.y==0].age, rwidth=.8, bins=np.linspace(0,100,100), color='b', alpha=.3, density=True)
plt.title("Não fez o depósito")

x=np.linspace(0,100,300)
plt.plot(x, norm.pdf(x,media_n,std_n),'b-');

"""**Exemplos**

* $P(idade=30|Y=0)$
"""

norm.pdf(30,media_n,std_n)

"""* $P(idade=30|Y=1)$"""

norm.pdf(30,media,std)

"""**Checando as contas...**

$P(Y|idade) = \frac{P(idade|Y) * P(Y)}{P(idade)}$
"""

idade=30

# P(Y)
p_y_1 = (df.y==1).mean() # prob de fazer o depósito
p_y_0 = (df.y==0).mean() # prob de não fazer o depósito

# prob Y=1 dado idade=30 (não normalizado)
p_y_1_idade_30 = norm.pdf(30,media,std) * p_y_1

# prob Y=0 dado idade=30 (não normalizado)
p_y_0_idade_30 = norm.pdf(30,media_n,std_n) * p_y_0

# normalizar: encontrar constante 1/P(idade)
c = 1.0/(p_y_1_idade_30+p_y_0_idade_30)

p_y_1_idade_30_NORM = p_y_1_idade_30*c
p_y_0_idade_30_NORM = p_y_0_idade_30*c

print("P(Y=1|idade=30) =",p_y_1_idade_30_NORM)
print("P(Y=0|idade=30) =",p_y_0_idade_30_NORM)

"""## Com o modelo

Não vamos separar em treino e teste porque usamos toda a tabela, mas o certo é ter os dois conjuntos. Essa aula é apenas para observar a diferença entre **categorical naive bayes** e **gaussian naive bayes**.
"""

gnb = GaussianNB()

gnb.fit(df[['age']],df.y) # variável pred é idade, variável resp é Y

# criar tabela de predições para a idade=30
pred = pd.DataFrame([30],columns=['age'])

pred

p=gnb.predict_proba(pred)

print("modelo")
print("P(Y=1|idade=30) =",p[0][1]) 
print("P(Y=0|idade=30) =",p[0][0])

print("\ncom as contas")
print("P(Y=1|idade=30) =",p_y_1_idade_30_NORM)
print("P(Y=0|idade=30) =",p_y_0_idade_30_NORM)

"""Podemos ver que os valores não são iguais, porém bastante próximos.

O modelo funciona bem para quando a distribuição é parecida com a normal, geralmente com variáveis numéricas.

Há vários modelos de aproximação, com formatos diferentes. No fundo, todos resolvem a equação do naive bayes, apenas assumindo distribuições diferentes para facilitar as contas.
"""