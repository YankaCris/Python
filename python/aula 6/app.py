familia = ["Milena" ,"Yanka","Joao","Adriana","Adriane" ] 
#            0          1       2      3         4
#            -5        - 4      -3     -2       -1



print(familia[3]) #retonar um indice
print(familia[-3]) #retorna um indicie de traz parafrente 
print(familia[2:])# retornar um indice a partit do indice 2
print(familia[2:4])# retornar a partir do indici até o 4, excluir o 4


print(familia)

familia[3] = "Caleb" # trocando com outro elemento da lista

print(familia)

familia[3]= "Adriana"

familia.extend(["Hadassa", "Fabricio", "Caleb"])#formal utilizar para adicionar +de 1 
print(familia)


familia.append("Gatinho") #adicionando apenas 1 e no final da lista
print(familia)


familia.insert(5,"Taiza") #inserindo + 1 em uma determinada posição da lista
print(familia)


familia.pop() #remover o ultimo da lista

familia.remove("Gatinho") # remove o valor determinado dentro dos parametros

familia.clear()# limpa toda lista

print(familia.index("Yanka")) # identificando a posição do nome na lista

print(familia.count("Yanka")) #Verifica quantos nomes tem iguais



