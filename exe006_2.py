from math import sqrt

num = int(input("Digite um número: "))

numP2 = num * 2
numP3 = num * 3
# A raiz quadrada de um número é o número elevado a 0,5 (n**1,5)
numRaiz = sqrt(num)

print(f'O dobro de {num} é {numP2}.\nO triplo de {num} é {numP3}.\nA raiz quadrada de {num} é igual a {numRaiz:.10}.')