
# aqui teremos um exemplo de distribuição de Probabilidade Binomial
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

n = 20
p = 0.5
x = np.arange(0, n+1)
binomial = binom.pmf(k=x, n=n, p=p)
plt.bar(x, binomial)
plt.xlabel('x', fontsize=12)
plt.ylabel('Probabilidade', fontsize=12)
plt.xlim([-1, n+1])
plt.title('Distribuição Binomial, n={0}, p={1}'.format(n,p), fontsize=15)
plt.show()