import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline seria demostrar me linha

#Gerando dados da população
tamanhoPopulacao = 10000
np.random.seed(2006)
dadosPopulacao = np.random.normal(loc = 100, scale = 10, size = tamanhoPopulacao)

plt.hist(dadosPopulacao)
plt.xlabel("Altura da parvore")
plt.ylabel("Quantidade de árvores")
plt.show()