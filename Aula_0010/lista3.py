list1 = ['physics', 'chemistry', 1997, 2000]
# print(list1)

# del deleta o valor do elemento nesse caso 1997
# del list1[2]
# print("After deleting value at index 2 : ")
# print(list1)

# del list1[2],list1[1]
# print(list1)


lista2 = ['banana', 'maçã','abacaxi','uva', 'morango']

lista2.remove('maçã')
lista2.remove('abacaxi')
lista2.append('cereja')
lista2.append('laranja')

# esse número 2 indica a posição do indice que será adicionado o valor
lista2.insert(2,'pêssego')

print(lista2)
