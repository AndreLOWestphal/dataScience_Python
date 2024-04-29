import pandas as pd
import prince
import matplotlib.pyplot as plt

dados = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data")
dados.columns = ['Color', 'Size', 'Action', 'Age', 'Inflated']
print(dados.head())

mAnaliseCorrespondencia = prince.MCA(n_components= 2)
mAnaliseCorrespondencia = mAnaliseCorrespondencia.fit(dados)

mAnaliseCorrespondencia.plot(dados)


