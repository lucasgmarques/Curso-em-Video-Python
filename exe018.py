import math

x = float(input("Digite o ângulo: "))

if (x == 90):
    print("Olha, ângulo reto!")

cosseno = math.cos(math.radians(x))
seno = math.sin(math.radians(x))
tangente = math.tan(math.radians(x))

print(f'Cosseno de {x} = {cosseno:.2f}')
print(f'Seno de {x} = {seno:.2f}')
print(f'Tangente de {x} = {tangente:.2f}')
