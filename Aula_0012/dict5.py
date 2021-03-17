dict_celulares = {"Modelo": "Galaxy S20",
                  "Fabricante": "Samsung", 
                  "Preço": "R$ 3100.00"}
# Quantidade de Chave-Valor do dicionário
# print(len(dict_celulares))
# Converte o dicionário para String
# print(str(dict_celulares))
# Mostra o tipo de dado da variável
# print(type(dict_celulares))
# Apaga as Chaves-Valores do dicionário
# dict_celulares.clear()
# print(dict_celulares)
# #Cópia do dicionário para outra variável
# new_dict = dict_celulares.copy()
# print(new_dict)
# #Cria um dicionário só com chaves e valores em None
# seq = ('Modelo', 'Fabricante', 'Preço')
# new1_dict = dict.fromkeys(seq)
# print(new1_dict)
# Get para pegar um valor dado uma chave, caso a chave não exista, o programa continua
# Também é possível atribuir um valor padrão para a chave não existente
# print(dict_celulares.get("Modelo"))
# print(dict_celulares.get("Tamanho", "Grande"))
# print(dict_celulares["Tamanho"]) #<===Da erro pq não existe
# Dicionário has_key não existe em python 3
# check = dict_celulares.has_key("Modelo")
# Exporta uma lista com Chaves e Valores no formato Tupla
# print(dict_celulares.items())
# Dicionarios de chaves e valores
# print(dict_celulares.keys())
print(dict_celulares.values())
