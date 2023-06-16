valor = float(input("Digite o valor da venda: "))
p = int(input("Digite o numero de parcelas: "))

final = valor/p

print("R$ {:.2f}".format(final))