#calculadora basica


print("----- Calculando--------")
print("Será exibido a soma, mult, divi, subtr dos números digitados")
num1 = int(input("Digit um número: "))
num2 = int(input("Digite outro numero: "))

res_soma = num1 + num2
res_sub = num1 - num2
res_div = num1 / num2
res_mult = num1 * num2

print("-------------------------")
print(f"RESULTADO\n Soma : {res_soma} \n Divisão :  {res_div} \n Subtração :  {res_sub} \n Multiplicação: {res_mult}" )
print("__________________________")