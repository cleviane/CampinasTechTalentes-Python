def printme(str):
   "This prints a passed string into this function"
   print(str)
   


def calcula_soma(num1, num2):
    result = num1 + num2
    return result

# printme("Oi, eu sou o Goku!")
numero1 = int(input("Digite o número 1\n"))
numero2 = int(input("Digite o número 2\n"))

resultado = calcula_soma(num1=numero1,num2=numero2)

print(f"O Resultado é {resultado}")
