
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# remove o valor "Zara"
# del dict['Name']  # remove entry with key 'Name'

# # remove as entradas, mas nao exclui o dicionario
# dict.clear()     # remove all entries in dict

# # deleta toda a chave
# del dict         # delete entire dictionary

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

dict_compras = {'Name':"Secador de cabelo","Preço": "R$1000,00", "Tamanho":"Médio"}
#exclui todos os elementos mas não exclui o dicionário da memória
# dict_compras.clear()
# print(dict_compras)
#Exclui o dicionário da memória
# del dict_compras
# print(dict_compras)
#Excluí um elemento do dicionário

del dict_compras["Name"]
print(dict_compras)
