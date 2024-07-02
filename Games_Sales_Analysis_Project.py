"""PROJETO DE ANÁLISE DE VENDAS DE GAMES DO PS4"""

'''Importação de bibliotecas necessárias para o projeto'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import style
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

'''Leitura e armazenamento dos dados a partir de um arquivo csv'''
Data_Base=pd.read_csv('PS4_GamesSales.csv', encoding='latin-1')
print(Data_Base.head())
print(Data_Base.describe())


plt.figure(figsize=(15,8))

'''Verificação de Dados Nulos, Tipos de Dados e Dimensão do Dataset'''
print(Data_Base.info())
plt.subplot(3,3,1)
sns.heatmap(Data_Base.isnull(), cbar=False)
plt.title('Análise de Dados Nulos', fontsize=9)
plt.xticks(rotation=45, ha='right')


'''Eliminação de amostras com dados faltantes'''
Data_Base.dropna(inplace=True)

'''Transformando a coluna Year de reais para inteiros'''
Data_Base['Year']=Data_Base['Year'].apply(lambda x: int(x))


'''Anál1ise do número de vendas de games ao longo dos anos'''
plt.subplot(3,3,2)
sns.barplot(data=Data_Base, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum)
plt.title('Análise do Número de Vendas de Games no tempo', fontsize=9)
plt.xlabel('Número de Jogos Vendidos (mi)')
plt.xticks(rotation=45, ha='right')
print(Data_Base.groupby(by='Year')['Global'].sum()) #Imprime o total das vendas para cada ano

'''Eliminando amostras que estão com dados zerados, que são amostras dos anos de 2019 e 2020'''
Data_Base=Data_Base.loc[ (Data_Base['Year']!=2019) & (Data_Base['Year']!=2020) ]

'''Análise da Distribuição do Número de Vendas Globais'''
plt.style.use('ggplot')
plt.subplot(3,3,3)
plt.title('Análise da Distribuição das Vendas Globais', fontsize=9)
plt.xlabel('Global (mi)')
sns.kdeplot(Data_Base['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5) #Distribuição de probabilidade(densidade) dos dados' shade e bw são paraâmetros do sombreamento

'''Análise da Distribuição do Número de Vendas Globais no Tempo'''
print(Data_Base.groupby(by='Year').sum())
plt.subplot(3,3,(4,7))
plt.title('Análise da Distribuição das Vendas Globais no Tempo', fontsize=9)
sns.boxplot(data=Data_Base, x='Year', y='Global')

'''Análise da Distribuição do Número de Vendas por continentes'''
Analysis=Data_Base.groupby(by='Year').sum()
N_America=[(N_America/Total)*100 for N_America, Total in zip(Analysis['North America'], Analysis['Global'])]
Europe=[(Europe/Total)*100 for Europe, Total in zip(Analysis['Europe'], Analysis['Global'])]
Japan=[(Japan/Total)*100 for Japan, Total in zip(Analysis['Japan'], Analysis['Global'])]
R_World=[(R_World/Total)*100 for R_World, Total in zip(Analysis['Rest of World'], Analysis['Global'])]
Global=[(Global/Total)*100 for Global, Total in zip(Analysis['Global'], Analysis['Global'])]
Years=list(Analysis.index)

plt.subplot(3,3,(5,6))
plt.bar(Years, N_America)
plt.bar(Years, Europe, bottom=N_America)
plt.bar(Years, Japan, bottom=[A+B for A,B in zip(N_America, Europe)])
plt.bar(Years, R_World, bottom=[A+B+C for A,B,C in zip(N_America, Europe, Japan)])
plt.title('Análise da Distribuição do Percentual de Vendas por Continentes', fontsize=9)
plt.ylabel('Distribuição Vendas (%)')
plt.legend(['North America', 'Europe', 'Japan', 'Rest of World'], loc='upper left', bbox_to_anchor=(0.15, -0.15), ncol=4)


'''Análise do Número de Vendas Mundiais para os principais publishers de jogos'''

Data_Base['Publisher Number']=le.fit_transform(Data_Base['Publisher'])

plt.subplot(3,3, (8,9))
plt.title('Análise da Distribuição de Vendas por Publishers', fontsize=9)
sns.scatterplot(data=Data_Base, x='Publisher Number', y='Global')


plt.tight_layout()
plt.show()



'''QUAIS OS TOP5 JOGOS MAIS VENDIDOS NO PERIODO '''
#(Data_Base.groupby(by='Games').sum())