
try:
  numero = int (input("Digite um número :"))


  print(numero)
except ZeroDivisionError:
    print("Essa divisão por 0 não possível!")
except ValueError:
    print("Digite um valor valido!")
except:
    print("Diigite um valor válido")

finally:
    print("Executar sempre!")