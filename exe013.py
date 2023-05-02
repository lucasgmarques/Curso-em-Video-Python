salarioAtual = float(input("Qual é o salário do funcionário?R$ "))
reajusteSalario = float(input("Quantos % é o reajuste salarial do funcionário? "))

novoSalario = salarioAtual + (salarioAtual * reajusteSalario / 100) 

print(f'Um funcionário que ganhava R${salarioAtual:.2f}, com {reajusteSalario}% de aumento, passa a receber R${novoSalario:.2f}')
