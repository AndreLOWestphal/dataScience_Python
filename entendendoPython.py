# Aqui imprimi-se o que se deseja

print('Olá Mundo')

# Deixarei varios exemplosde print abaixo de strings com numbers

print(12345)
print('valor',12345)
print('valor = {}'.format(123456))
print(f'valor = {1234}')
print("valor",12345)
print("valor = {}".format(123456))
print(f"valor = {1234}")

# Abaixo concatenção de strings criado por variaveis

nome1 = 'vamos aprender python'
print(nome1)
print('valor da variavel nome = {}'.format(nome1))
print(f'valor da variavel nome = {nome1}')
print(f"valor da variavel nome = {nome1}")

# Abaixo concatenção de numbers criado por variaveis

numero1 = 1574256
print(numero1)
print('valor da variavel numero = {}'.format(numero1))
print(f'valor da variavel numero = {numero1}')
print(f"valor da variavel numero = {numero1}")

# Abaixo utilizamos unput e solicitamos um numero inteiro

valor1 = int(input("Entre com um numero: "))

# Agora com exemplos de condicional sem funções

#ex:1
a1 = 50

if a1 < 80:
    a1 = a1 + 7
print (f'a = {a1}')

#ex:2
a2 = 780

if(a2%2 == 0):
    print(f'{a2} é par!')
else:
    print(f'{a2} é impar!')
    
# abaixo iremos para exmeplos de loop

#ex:1
contador = 0
s1 = ''

while (contador < 10):
    s1 = s1 + str(contador) + ' '
    contador = contador + 1
print(s1)

#ex:2
s2 = ''
for contador in range(10):
    s2 = s2 + str(contador) + ' '
print(s2)

# trabalhando com listas array

#ex:01
lista1 = [50,55,56,86,98,158,200]

print(lista1)
print(f'lista[0] = {lista1[0]} e lista[5] = {lista1[5]}')

# aqui temos indexação explícita da lista
n1 = len(lista1)
s3 = ''

for i in range(n1):
    s3 = s3 + str(lista1[i])+ ' '
print(s3)

# neste exemplo temos um paradgma funcional
s4 = ''

for a in lista1:
    s4 = s4 + str(a) + ' '
print(s4)

# Abaixo trabalharemos com função e como montar sua estrutura.
def encontrarMinimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo

listaTeste = [25,10,57,48,65,32,24,12]
menor = encontrarMinimo(listaTeste)
print('O menor elemento da lista é:[{}]'.format(menor))