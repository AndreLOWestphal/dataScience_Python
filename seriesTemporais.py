import numpy as np

dadosOriginais = [3,5,1,6,7,8,6,9,9,10]

tamanhoJanela = 3
pesos = np.repeat(1.0,tamanhoJanela) / tamanhoJanela
mediasMoveis = np.convolve(dadosOriginais, pesos,"valid")

print("Médias móveis: {}".format(np.round(mediasMoveis,2)))