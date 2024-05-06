import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import OneHotEncoder

# Carregar os dados
a = pd.read_csv('vinhos.csv', delimiter=";")

# Codificar variáveis categóricas
encoder = OneHotEncoder()
encoded_columns = encoder.fit_transform(a[['VINHO', 'TIPO', 'COR', 'CHEIRO']])

# Converter as colunas codificadas em um DataFrame e concatenar com o DataFrame original
encoded_df = pd.DataFrame(encoded_columns.toarray(), columns=encoder.get_feature_names_out(['VINHO', 'TIPO', 'COR', 'CHEIRO']))
a = pd.concat([a, encoded_df], axis=1)

# Remover as colunas originais que foram codificadas
a.drop(['VINHO', 'TIPO', 'COR', 'CHEIRO'], axis=1, inplace=True)

# Separar features e target
y = a['ESTILO']
x = a.drop('ESTILO', axis=1)

# Dividir os dados em conjuntos de treino e teste
xTreino, xTeste, yTreino, yTeste = train_test_split(x, y, test_size=0.3)

# Instanciar e treinar o modelo
modelo = ExtraTreesClassifier()
modelo.fit(xTreino, yTreino)

# Avaliar o modelo
resultado = modelo.score(xTeste, yTeste)
print('Acuracia: ', resultado)
print(modelo.fit)