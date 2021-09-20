import datetime

anoAtual = datetime.date.today().year

print("Olá, seja bem vindo!\n")
nome = input("Digite seu nome: ")
anoPessoa = int(input("Digite o ano do seu nascimento: "))
idade = anoAtual - anoPessoa
print("Olá, {}. Sua idade é {}.".format(nome,idade))
