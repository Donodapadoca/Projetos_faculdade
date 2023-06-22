import math

a = float(input("Digite o valor de a (a ≠ 0): "))
if a==0:
    a = float(input("Digite um novo valor para a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = float(input("Digite o valor de x: "))

# Cálculo das raízes
delta = b**2 - 4*a*c
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

# Cálculo de ax^2 + bx + c
valor = a*x**2 + b*x + c

# Exibição dos resultados
print("Primeira raiz:", raiz1)
print("Segunda raiz:", raiz2)
print("Valor de x + bx + c:", valor)
