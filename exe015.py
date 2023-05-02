diasAlugados = int(input("Quantos dias alugados? "))
kmRodados = float(input("Quantos dias rodados? "))
diaria = float(input("Quanto custa a diária? "))
custoKM = float(input("Quanto custa p/ km rodado? "))

custoTotal = (diasAlugados * diaria) + (kmRodados * custoKM)

print("O total a pagar é de R${:.2f}".format(custoTotal))
