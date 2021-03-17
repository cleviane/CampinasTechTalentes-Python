
list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ")
print(list[2])

list[2] = 2001
print("New value available at index 2 : ")
print(list[2])

# append adiciona um valor na lista, e sempre adiciona o valor no final
list.append("hahaha")
list.append(["ajajaja", 1995])
list.append({'Chave': 'valor', 'OutraChave': 'OutroValor'})
list.append(["valor1", "valor2"])
print(list)
