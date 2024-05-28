import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x, y = load_iris(return_X_y=True)
print(f'dimensões de X={x.shape}, comprimento de y={y.shape}')

xTreino, xTeste, yTreino, yTeste = train_test_split(x, y, test_size=0.3, random_state=0)

modelo = LogisticRegression(multi_class='multinomial', solver='lbfgs')

modelo.fit(xTreino, yTreino)

yPred = modelo.predict(xTeste)

precisao = accuracy_score(yTeste, yPred)
print(f'Precisao = {precisao}')

yPrevisto = modelo.predict(xTeste[[7]])
yReal = yTeste[7]
print(f'Real = {yReal}, Previsto = {yPrevisto}')