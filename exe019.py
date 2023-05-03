from random import choice

nomes = []
nomes.append(input("Digite o primeiro aluno: "))
nomes.append(input("Digite o segundo aluno: "))
nomes.append(input("Digite o terceiro aluno: "))
nomes.append(input("Digite o quarto aluno: "))

sorteio = choice(nomes)

print(f'O aluno escolhido foi {sorteio}')
