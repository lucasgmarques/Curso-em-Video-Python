verificaAlgo = input("Digite alguma coisa: ")
print(f'Você digitou: {verificaAlgo}')
print(f'Seu tipo é {type(verificaAlgo)}')
print(f'É alfanumérico? {verificaAlgo.isalnum()}')
print(f'É alfabético? {verificaAlgo.isalpha()}')
print(f'É numérico? {verificaAlgo.isnumeric()}')
print(f'Só tem espaços? {verificaAlgo.isspace()}') 
print(f'Está em maiúscula? {verificaAlgo.isupper()}')

