import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x=[10,15,16,18]
y=[100,180,200,300]

modeloPolinomial = np.poly1d(np.polyfit(x,y,3))
linha = np.linspace(1,22,100)

plt.scatter(x,y,c="red")
plt.plot(linha, modeloPolinomial(linha))
plt.show()