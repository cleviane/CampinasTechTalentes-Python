nome = "João"
ispessoa = True
iteracao = 0


while iteracao <= 10:
    iteracao = iteracao + 1
    if iteracao == 4:
    #    break conta até 4
         continue # continua a contagem até o final
    print(f"Meu nome é {nome} {iteracao}")

print("fim programa")