real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolarHoje = float(input("Qual a cotação do dólar hoje: "))
euroHoje = float(input("Qual a cotação do Euro hoje: "))
dolar = real / dolarHoje
euro = real / euroHoje
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} ou EUR{euro:.2f}')