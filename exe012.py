preco_produto = float(input("Qual o preço do produto? R$"))
percentual_desconto = float(input("Qual a taxa de desconto? "))

# CALCULO DO DESCONTO
desconto_prod = preco_produto - (preco_produto * percentual_desconto/100)

print(f'O produto que custava R${preco_produto:.2f}, na promoção com desconto de {percentual_desconto:.0f}% vai custar R${desconto_prod:.2f}')