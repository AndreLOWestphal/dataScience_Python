import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url="https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)
df.head()
df.describe().round(1)
df = df.dropna()
print(df.head())
print(df.describe().round(1))

plt.hist(df['Sex'])
plt.xlabel('Categorias')
plt.ylabel('Quantidades')
plt.hist(x=df['Sex'],
         bins='auto',
         color='#0867aa',
         alpha=0.7,
         rwidth=0.35,
         density=True)
plt.grid(axis='y',
         alpha=0.8)
plt.xlabel('Categorias')
plt.ylabel('Quantidades')
plt.title('Histograma de Pessoas Sobreviventes')
plt.show()