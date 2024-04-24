import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

#Gerar dados para população como exemplo
tamanhoPopulacao = 10000
np.random.seed(2000)

listaDados = []
for i in range(2):
    dados = np.random.normal(loc=100, scale=10, size=tamanhoPopulacao)
    listaDados.append(dados)

dados1 = listaDados[0]
dados2 = listaDados[1]

estatistica, p_valor, = ttest_ind(dados1,dados2)
print('estatistica=%.3f, p_valor=%.3f' % (estatistica, p_valor))


if p_valor > 5/100:
    print('Aceita H0')
else:
    print('Rejeita H1')

plt.hist(dados)
plt.ylabel('Quantidades')
plt.hist(x=dados, bins='auto', color='#0805aa', alpha=0.7, rwidth=0.85, density=True)
plt.grid(axis="y", alpha=0.80)
plt.xlabel('Categorias')
plt.ylabel('quantidades')
plt.title('Histograma das Amostras')
plt.show()