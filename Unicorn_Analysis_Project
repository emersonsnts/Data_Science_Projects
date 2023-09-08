"""PROJETO DE ANÁLISE DE DADOS DE STARTUPS UNICÓRNIOS"""

'''Importacão de bibliotecas necessárias para o projeto'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') #Ignora avisos 


'''INÍCIO'''
print('\033[1;32mANÁLISE DE DADOS DE STARTUPS UNICÓRNIOS\33[m\n')


'''Leitura e armazenamento dos dados a partir de um arquivo csv'''
Data_Base=pd.read_csv('unicorns till sep 2022.csv')


'''Edição dos nome das variáveis (colunas) do banco de dados'''
Data_Base.rename(columns={
    'Company':'Empresa',
    'Valuation ($B)':'Valor ($B)',
    'Date Joined': 'Data de Adesão',
    'Country':'País',
    'City ':'Cidade',
    'Industry':'Setor',
    'Investors':'Investidores'
}, inplace=True)

plt.figure(figsize=(18,10))

'''Verificação de Dados Nulos'''
print('\033[7;32m INFORMAÇÕES GERAIS SOBRE OS DADOS \33[m')
print(f' {Data_Base.info()}') #Imprime informacões gerais sobre os dados
print('\n\033[7;32m QUANTIDADE DE DADOS NULOS POR VARIÁVEL \33[m \n', Data_Base.isnull().sum()) #Imprime a quantidade de dados nulos em cada variável (coluna)
plt.subplot(3,3,1)
sns.heatmap(Data_Base.isnull(), cbar=False) #Cria um HeatMap da relação entre o id dos dados nulos e as variáveis(colunas)
plt.title('Análise de Dados Nulos', fontsize=10)
plt.xticks(rotation=35, ha='right')
plt.ylabel('Index')


'''Análise Setorial'''
print('\n\033[7;32m QUANTIDADE DE DADOS ÚNICOS POR VARIÁVEL \33[m\n', Data_Base.nunique()) #Imprime o número de dados unicos por coluna. Base_Dados['Column name'].nunique() para especificar uma coluna.
print('\n\033[7;32m NÚMERO DE UNICÓRNIOS POR SETOR \33[m \n', Data_Base['Setor'].value_counts().head()) #Imprime a frequência absoluta dos dados únicos para cada categoria(coluna). Base_Dados['Setor'].value_counts(normalize=True) para imprimir a frequência relativa.
plt.subplot(3,3,2)
plt.bar(Data_Base['Setor'].value_counts().index[:10], Data_Base['Setor'].value_counts(normalize=True).head(10)*100) #Criando um grafico de barras dos top 10 setores
plt.ylabel('(%) Participação')
plt.title('Análise Setorial de Unicórnios', fontsize=10)
plt.xticks(rotation=35, ha='right')


'''Criação de um gráfico pizza dos top 6 paises geradores de Startups Unicórnios'''
plt.subplot(3,3,3)
plt.title('Análise de Paises Geradores de Unicórnios', fontsize=10)
plt.pie(round(Data_Base['País'].value_counts(normalize=True)*100,1).head(6),
        shadow=True,
        startangle=90,
        autopct='%1.0f%%',
        radius=1.2,
        pctdistance=0.9,
        textprops={'fontsize':6}
)
plt.legend((Data_Base['País'].value_counts(normalize=True).index[:6]), title="Países", loc="center left", bbox_to_anchor=(1.1, 0, 0.5, 1))


'''Conversão de um dado de data em formato string para datetime'''
Data_Base['Data de Adesão']=pd.to_datetime(Data_Base['Data de Adesão'])
Data_Base['Mês']=pd.DatetimeIndex(Data_Base['Data de Adesão']).month #Criando novas colunas com informaçoes de data de mês e ano
Data_Base['Ano']=pd.DatetimeIndex(Data_Base['Data de Adesão']).year


'''Tabelas Analíticas: agrupando por país, ano e empresa, contando a frequência apenas de uma coluna específica'''
Group_Co_Ye_Ca_In=Data_Base.groupby(by=['País', 'Ano', 'Empresa']).count()['Investidores'].reset_index() #O parãmetro reset_index() serve para preencher as lacunas da árvore com os respectivos nomes das variáveis, isto é, transformar a árvore em tabela
print('\n\033[7;32m AGRUPAMENTO POR (PAÍS)->(ANO DE ADESÃO)->(EMPRESA)->(NÚMERO DE INVESTIDORES)\33[m\n', Group_Co_Ye_Ca_In)
print('\n\033[7;32m AGRUPAMENTO DOS UNICÓRNIOS DO BRASIL POR (ANO DE ADESÃO)->(EMPRESA)->(NÚMERO DE INVESTIDORES)\33[m\n', Group_Co_Ye_Ca_In.loc[Group_Co_Ye_Ca_In['País']=='Brazil'].head())  #extraindo as informações somente do Brasil


'''Transformando a coluna Valor($) de string to flot para que se possa criar gráficos envolvendo essa variável'''
Data_Base['Valor ($B)']=pd.to_numeric(Data_Base['Valor ($B)'].apply(lambda linha: linha.replace('$', '')))
Group_Co_Va=Data_Base.groupby(by=['País']).sum('Valor ($B)')['Valor ($B)'].reset_index().sort_values('Valor ($B)', ascending=False) #Criando um ranking dos países em relação ao valuetion do mercado de unicornios
print('\n\033[7;32m RANKING DOS TOP10 PAÍSES COM MAIORES VALUATION EM UNICÓRNIOS \33[m\n', Group_Co_Va[:10])
plt.subplot(3,3,4)
plt.title('Análise de Valor dos TOP10 Países em Unicórnios', fontsize=10)
plt.ylabel('$BI')
plt.bar(Group_Co_Va['País'][:10], Group_Co_Va['Valor ($B)'][:10])
plt.xticks(rotation=35, ha='right')


'''ANÁLISES EXTRAS'''


'''ANÁLISE DE QUAL UNICÓRNIO TEM MAIOR NÚMERO DE INVESTIDORES DO MUNDO'''
Data_Base['Investidores em Lista']=Data_Base['Investidores'].apply([lambda investidores: str(investidores).split(',')])
Data_Base['Número de Investidores']=Data_Base['Investidores em Lista'].apply(lambda x: len(x))

plt.subplot(3,3,5)
plt.hist(Data_Base['Número de Investidores'], bins=[1,2,3,4,5])
plt.title('Análise do Nº de Investidores por Unicórnios', fontsize=10)
plt.ylabel('Unicórnios')
plt.xlabel('Investidores por Unicórnio')
plt.xticks(range(0,max(Data_Base['Número de Investidores'])+1))


'''ANÁLISE DE QUAIS OS MAIORES INVESTIDORES DO MUNDO EM UNICÓRNIOS'''
List_Investidores=list()
for i in Data_Base['Investidores em Lista']:
    for j in i:
        List_Investidores.append(j)
Data_Series_Investidores=pd.Series(List_Investidores)

plt.subplot(3,3,6)
plt.bar(Data_Series_Investidores.value_counts().index[:10], Data_Series_Investidores.value_counts()[:10])
plt.ylabel('Unicórnios Investidos')
plt.title('Análise dos TOP10 Maiores Investidores em Nº de Unicórnios', fontsize=10)
plt.xticks(rotation=35, ha='right' )
plt.subplots_adjust(left=0.09,
                    bottom=0.05,
                    right=0.88,
                    top=0.95,
                    wspace=0.4,
                    hspace=1)
plt.show()






