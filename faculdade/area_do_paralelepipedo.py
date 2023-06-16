a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

V = a*b*c
D = ((a**2)*(b**2)*(c**2))**2

print("volume: {:.2f}".format(V))
print("Diargonal: {:.2f}".format(D))