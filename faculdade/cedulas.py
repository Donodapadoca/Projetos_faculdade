def decompor_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_cedulas = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(cedulas)):
        quantidade_cedulas[i] = valor // cedulas[i]
        valor %= cedulas[i]

    return quantidade_cedulas

valor_reais = int(input("Digite o valor em reais: "))

quantidade_cedulas = decompor_cedulas(valor_reais)

print("Quantidade de cédulas:")
print(" notas de 100:", quantidade_cedulas[0])
print(" notas de 50:", quantidade_cedulas[1])
print(" notas de 20:", quantidade_cedulas[2])
print(" notas de 10:", quantidade_cedulas[3])
print(" notas de 5:", quantidade_cedulas[4])
print(" notas de 2:", quantidade_cedulas[5])
print(" notas de 1:", quantidade_cedulas[6])
