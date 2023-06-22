nome = input("Digite o nome do vendedor: ")

salario = float(input("Digite o salario: "))

vendas = float(input("Digite a qtd de vendas: "))

porcent = int(input("Digite a porcentagem das vendas: "))


final = salario+(vendas*(porcent/100))


print(nome, "deve receber R${:.2f}".format(final))