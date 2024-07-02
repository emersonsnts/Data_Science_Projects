'''ANÁLISE DE DADOS DA EDUCAÇÃO'''


'''Importação das bibliotecas necessárias para o projeto '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

'''Leitura e Armazenamento de dados a partir de um arquivo csv'''
Data_Base=pd.read_csv('StudentsPerformance.csv')

'''Verificação de Dados Nulos'''
plt.figure(figsize=(15,8))
plt.subplot(3,3,6)
sns.heatmap(Data_Base.isnull(), cbar=False)
plt.xticks(rotation=45, ha='right', fontsize=8)



'''
#Data_Base.isnull().sum() #Mostra o número de dados nulos por coluna
#print(Data_Base.duplicated().sum()) #Mostra o número de linhas duplicadas
print(Data_Base.info())
print(Data_Base['gender'].value_counts(normalize=True)*100)
print(Data_Base['race/ethnicity'].value_counts(normalize=True)*100)
print(Data_Base['parental level of education'].value_counts(normalize=True)*100)
print(Data_Base['lunch'].value_counts(normalize=True)*100)
print(Data_Base['test preparation course'].value_counts(normalize=True)*100)
'''

print(f'{Data_Base.columns} \n')

'''HOMENS OU MULHERES TEM MAIOR PRÉ-DISPOSIÇÃO PARA DETERMINADA DISCIPLINA? '''

print('\nDescricão geral por gênero: \n', Data_Base.groupby(by='gender').describe().reset_index())

plt.subplot(3,3,1)
sns.boxplot(data=Data_Base, x='math score', y='gender')
print('\nDescricão de math score por gênero \n', Data_Base.groupby(by='gender').describe()['math score'].reset_index())

plt.subplot(3,3,2)
sns.boxplot(data=Data_Base, x='reading score', y='gender')
print('\nDescricão de reading score por gênero \n', Data_Base.groupby(by='gender').describe()['reading score'].reset_index())


plt.subplot(3,3,3)
sns.boxplot(data=Data_Base, x='writing score', y='gender')
print('\nDescricão de writing score por gênero \n', Data_Base.groupby(by='gender').describe()['writing score'].reset_index())


'''CRIANDO UMA COLUNA ADICIONAL DA MÉDIA DAS 3 DISCIPLINAS'''
general_mean=[]
for i in range(len(Data_Base['math score'])):
    general_mean.append(round(np.average([Data_Base['math score'][i],
                                    Data_Base['reading score'][i],
                                    Data_Base['writing score'][i]])))
Data_Base['general_mean']=pd.Series(general_mean)


'''O NÍVEL DE ESCOLARIDADE DOS PAIS INFLUENCIA NO DESEMPENHO ESCOLAR?'''
plt.subplot(3,3,4)
sns.boxplot(data=Data_Base, x='general_mean', y='parental level of education')
print('\n Descrição das notas em relação ao nível de escolaridade dos pais',Data_Base.groupby(by='parental level of education').describe().reset_index())


'''FAZER O TESTE DE PREPARAÇÃO INFLUENCIA NAS NOTAS?'''
plt.subplot(3,3,5)
sns.boxplot(data=Data_Base, x='general_mean', y='test preparation course')
print('Descrição dos notas em relação ao teste de preparação', Data_Base.groupby(by='test preparation course').describe().reset_index())


sns.pairplot(Data_Base, hue='race/ethnicity') #gráfico cruzado de todas as variáveis


plt.tight_layout()
plt.show()


sns.swarmplot(data=Data_Base, x='race/ethnicity', y='math score')
plt.show()
sns.violinplot(data=Data_Base, x='race/ethnicity', y='math score')
plt.show()