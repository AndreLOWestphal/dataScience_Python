import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#variaveis
dados = np.array([[-1.5,-1.5],[-2.3,-2.1],[-3.1,-2.7],[1.6,1.2],[2.3,1.5],[3.1,2.5]])

grupos = np.array([1,1,1,2,2,2])

#Analise
clf = LinearDiscriminantAnalysis()
clf.fit(dados,grupos)

#teste
dadosTeste=[0.0,0.0]
grupoResultado=clf.predict([dadosTeste])
print(f'Os dados de teste {dadosTeste} pertencem ao grupo {grupoResultado}')

#grafico
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(dados[:,0],dados[:,1], c=grupos,cmap="rainbow",alpha=0.9, edgecolors="b")
plt.scatter(dadosTeste[0], dadosTeste[1], c="yellow", linewidths=2,marker="^", edgecolors="red", s = 200)
plt.title("Análise Linear Discriminante")
plt.show()