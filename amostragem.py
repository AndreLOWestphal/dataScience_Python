import numpy as np
import matplotlib.pyplot as plt

tamanhoPopulacao = 10000
np.random.seed(2006)
dadosPopulacao = np.random.normal(loc = 100, scale = 10, size = tamanhoPopulacao)

tamanhoAmostra = 50
qtdSimulacoes = 10
mediasAmostras = []

for x in range (qtdSimulacoes):
    mediaAmostra = np.random.choice(dadosPopulacao, size = tamanhoAmostra).mean()
    mediasAmostras.append(mediaAmostra)
mediasAmostras = np.array(mediasAmostras)

plt.hist(x=mediasAmostras, bins='auto', color='#0705ba', alpha=0.7, rwidth=0.85, density=True)
plt.grid(axis='y', alpha=0.80)
plt.xlabel("Médias das alturas das amostras")
plt.ylabel("Frequência de ocorrência")
plt.title("Histograma das Médias das Amostras")
plt.show()