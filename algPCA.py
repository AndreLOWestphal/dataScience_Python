import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#dados a respeito do cancêr de mama para trabalharmos
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
df = pd.DataFrame(cancer['data'], columns= cancer['feature_names'])
view = df.head(10)

print(view)
print(f'dimensões: {df.shape}')

#para padronizar os dados usaremos:
from sklearn.preprocessing import StandardScaler

escalar = StandardScaler()
escalar.fit(df)
dadosEscalados = escalar.transform(df)

print(dadosEscalados)

from sklearn.decomposition import PCA
pca = PCA(n_components= 2)
pca.fit(dadosEscalados)
xPca = pca.transform(dadosEscalados)

print(xPca)
print(xPca.shape)

#começamos aqui a etapa dos graficos
plt.figure(figsize=(8,6))
plt.scatter(xPca[:,0], xPca[:,1],
            c = cancer['target'],
            cmap='plasma')
plt.xlabel('Primeiro Componente Principal')
plt.ylabel('Segundo Componente Principal')
plt.show()