from random import shuffle

# Inicializa uma lista vazia
nomes = []

nomes.append(input("Digite o nome do primeiro aluno: "))
nomes.append(input("Digite o nome do segundo aluno: "))
nomes.append(input("Digite o nome do terceiro aluno: "))
nomes.append(input("Digite o nome do quarto aluno: "))

# Embaralha a sequencia de itens da lista
sorteio = shuffle(nomes)

for i, nome in enumerate(nomes):
    print(f'O(a) aluno(a) {nome} será o {i+1}º na ordem de apresentação!')

