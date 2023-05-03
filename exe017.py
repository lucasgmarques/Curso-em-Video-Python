import math

catOposto = float(input("Qual o comprimento do cateto oposto? "))
catAdj = float(input("Qual o comprimento do cateto adjacente? "))

# hiponetusa = math.sqrt(catOposto * catOposto + catAdj * catAdj)

print(f'O comprimento da hiponetusa é: {math.hypot(catOposto, catAdj)}')
# print(hiponetusa)


