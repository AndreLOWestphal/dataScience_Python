import scipy.stats as st

# Estimação de Parametros
nvlConfianca = 95/100
nvlSignificancia = 1 - nvlConfianca
Z = abs(st.norm.ppf(nvlSignificancia/2))

print(f'Z={Z}')

#Intervalo de Confiança
import math

tamanhoPopulacao = 60
desvioPadrao = 2/100
desvioPadraoAmostral = desvioPadrao/math.sqrt(tamanhoPopulacao)
mediaAmostral = 1/100
limSuperior = mediaAmostral + Z*desvioPadraoAmostral
limInferior = mediaAmostral - Z*desvioPadraoAmostral
intervaloConfianca = (mediaAmostral - limInferior, mediaAmostral + limSuperior)

print(f'Intervalo de Confiança={intervaloConfianca}')