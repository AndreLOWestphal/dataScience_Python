from sklearn import tree
import matplotlib.pyplot as plt

dados = [[0,0],[1,1],[2,0],[1,3],[2,6],[3,2]]

rotulos = [0,1,0,1,1,1]

classificador= tree.DecisionTreeClassifier()
classificador= classificador.fit(dados, rotulos)

teste=[1.,2.]
resultado=classificador.predict([teste])
print(f'o dado {teste} foi classificado como {resultado}')

plt.Figure(figsize=(12,12))
tree.plot_tree(classificador, filled=True)
plt.show()