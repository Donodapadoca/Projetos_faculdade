x = int(input("Digite o valor em segundos: "))

horas = x // 3600
minutos = (x % 3600) // 60
segundos = (x % 3600) % 60

horafinal = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)

print("Tempo equivalente: ", horafinal)