a= int(input("Digite o valor de A: "))
b= int(input("Digite o valor de B:"))

if a<=0:
    a = int(input("Digite outro valor para A:"))
    
if b<=0:
    b = int(input("Digite outro valor para B: "))
    
    
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x==y:
    x = int(input("Digite outro valor para X: "))
    
final = a+(b**x)-(b**2)+(a+b)/(x-y)

print("expressão: {:.2f} ".format(final))
    