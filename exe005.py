num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

def soma_num(n1, n2):
    return n1 + n2

def sub_num(n1, n2):
    return n1 - n2

def multiplica_num(n1, n2):
    return n1 * n2

def divide_num(n1, n2):
    return n1 / n2

print(f'A soma dos números é {soma_num(num1, num2)} e a subtração dos valores é {sub_num(num1, num2)}')
print(f'A multiplicação dos valores é {multiplica_num(num1, num2)} e a divisão resultada {divide_num(num1, num2)}')