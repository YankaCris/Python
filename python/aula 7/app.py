#def big_mac():
   # print("Sanduiche big mac")

#print("Inicio")
#big_mac()
#print("Fim")

def fazer_big_mac(nome):
    print(f"Sanduiche big mac {nome}")

#fazer_big_mac("MIlena")
#fazer_big_mac("Yanka")

def fazer_batata(tamanho):
    print(tamanho)

def preparar_refri(tipo,tamanho):
    print(f"{tipo} {tamanho}")
    

#fazer_big_mac("Yanka")
#fazer_batata("Grande")
#preparar_refri("Coca","Média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac("Yanka")
    fazer_batata(tamanho_batata)
    preparar_refri(tipo_refri,tamanho_refri)

fazer_combo_big_mac("Yanka","Grande","Coca","Médio")


#somando 2 números 
def soma_numero(num1,num2):
    return num1 + num2

resultado = soma_numero(25,20)
print(resultado)


#retonando o maior número da lista

def maior_num(list_num):
    list_num.sort()
    list_num.reverse()
    maior_num = list_num[0]
    return maior_num

resultado = maior_num([123,254,263,45,172,3689,5486,321,5584])
print(resultado)
