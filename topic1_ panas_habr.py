import pandas as pd
import numpy as np

df = pd.read_csv('data/telecom_churn.csv')
df.head()
print('======RESULT df.shape======')
print(df.shape)
print('======RESULT df.columns======')
print(df.columns)
print('======RESULT df.info()======')
print(df.info())
df['Churn'] = df['Churn'].astype('int64') # converting column Churn from bool to int64
print('======RESULT df.describe()======')
print(df.describe())
print('======RESULT df.describe(inclide = object,bool) ======')
print(df.describe(include = ['object', 'bool'])) # A white list of data types to include in the result
print('======RESULT df[Churn].value_counts() ======')
print(df['Churn'].value_counts())
print('======RESULT df[Area code].value_counts() ======')
print(df['Area code'].value_counts())
print('======RESULT df[Area code].value_counts(normalize=True) ======')
print(df['Area code'].value_counts(normalize=True))
print('======RESULT of sorting by Total day charge ascending ======')
print(df.sort_values(by = 'Total day charge', ascending = False).head())
print('======RESULT of sorting by Churn, Total day charge, acending True, False ======')
print(df.sort_values(by=['Churn', 'Total day charge'], ascending=[True, False]))
print('======RESULT df[Churn].mean() ======')
print(df['Churn'].mean())
print('======RESULT df[df[Churn]] == 1].mean ======')
print(df[df['Churn'] == 1].mean())
print('======RESULT df[df[Churn] == 1][Total day minutes].mean ======')
print(df[df['Churn'] == 1]['Total day minutes'].mean())
print('======RESULT df[(df[Churn] == 1) & (df[International plan] == No)][Total intl minutes].max() ======')
print(df[(df['Churn'] == 1) & (df['International plan'] == 'No')]['Total intl minutes'].max())
print('======RESULT df.loc ======')
print(df.loc[0:5, 'State':'Area code'])
print('======RESULT df.iloc ======')
print(df.iloc[0:5,0:3])
print('======RESULT apply to each column np.max ======')
print(df.apply(np.max))
d = {'No' : False, 'Yes' : True}
# Map
df['International plan'] = df['International plan'].map(d)
# Replace
df = df.replace({'Voice mail plan':d})
# Groupby
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
print('======RESULT groupby Churn ======')
print(df.groupby(['Churn'])[columns_to_show].describe(percentiles=[]))
print(pd.crosstab(df['Churn'], df['International plan']))
print(pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True))
print(df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], 
['Area code'], aggfunc='mean').head(10))
