num = int(input("Digite um número: "))

print(f"A tabuada do {num}:")

for i in range(1,11):
    print(f'{num} x {i:2} = {num * i:2}')
