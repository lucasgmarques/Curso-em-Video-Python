precoAtual = float(input("Digite o preço do produto: R$"))
percentDesconto = float(input("Digite o percentual de desconto na compra à vista: "))
percentPrazo = float(input("Digite o percentual de acréscimo na compra à prazo: "))

precoDesconto = precoAtual - (precoAtual * percentDesconto / 100)
precoPrazo = precoAtual + (precoAtual * percentPrazo / 100)

print(f'O preço do produto à vista com {round(percentDesconto)}% de desconto fica {precoDesconto:.2f}')
print(f'O preço do produto à prazo com {round(percentPrazo)}% de acréscimo fica {precoPrazo:.2f}')

