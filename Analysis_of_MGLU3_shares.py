"""PROJETO DE ANÁLISE DAS AÇÕES NA BOLSA DA MAGALU"""

'''Importacão de bibliotecas necessárias para o projeto'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib import style
import warnings
warnings.filterwarnings('ignore')

'''Leitura e armazenamento dos dados a partir de um arquivo xlsx(excel)'''
Data_Base=pd.read_excel('Magalu_Shares_Dataset.xlsx')


'''Verificação de Dados Nulos, Tipos de Dados e Dimensão do Dataset'''
print(Data_Base.info())
plt.figure(figsize=(15,8))
plt.subplot(3,3,1)
plt.title('Análise de Dados Nulos')
sns.heatmap(Data_Base.isnull(), cbar=False)
plt.xticks(rotation=45, ha='right')

'''Análise gráfica do fechamento das ações da MAGALU durante todo o ano de 2021'''
Data_Base2=Data_Base.set_index('Data') #Transformando uma coluna como o index do dataset
plt.style.use('seaborn-darkgrid') #estilo de fundo do gráfico
plt.subplot(3,3,(2,3))
plt.title('Análise do fechamento das ações da MAGALU', fontsize=12)
plt.xlabel('Datas da Cotação')
plt.ylabel('Valor da Ação (R$)')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.plot(Data_Base2.index, Data_Base2['Fechamento'], label='MMA (1)')

'''Análise gráfica do fechamento das ações da MAGALU durante todo o ano de 2021 através de médias móveis de 5 e 30 dias'''
plt.plot(Data_Base2.index,Data_Base2['Fechamento'].rolling(5).mean(), label='MMA (5)')
plt.plot(Data_Base2.index,Data_Base2['Fechamento'].rolling(30).mean(), label='MMA (30)')
plt.legend(loc='lower left')


'''Análise gráfica do fechamento das ações da MAGALU durante todo o ano de 2021 mês a mês'''
Data_Base['Mês']=Data_Base['Data'].dt.month
print(Data_Base.groupby('Mês').describe()['Fechamento'])
plt.subplot(3,3,(4,9))
plt.title('Análise do fechamento das ações da MAGALU mês a mês, 2021')
sns.boxplot(data=Data_Base, x='Mês', y='Fechamento')

'''Análise gráfica do fechamento das ações da MAGALU durante todo o ano de 2021 através do gráfico estilo IBOVESPA'''
#Nota: A plotagem deste gráfico se dá externamente através da web
graph=go.Figure(
    data=[
        go.Candlestick(x=Data_Base2.index,
                       open=Data_Base2['Abertura'],
                       high=Data_Base2['Maior'],
                       low=Data_Base2['Menor'],
                       close=Data_Base2['Fechamento']



        )
    ]
)

graph.show()
plt.tight_layout()
plt.show()
