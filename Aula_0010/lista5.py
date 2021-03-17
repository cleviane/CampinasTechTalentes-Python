lista_suco =['laranja','uva','abacaxi','manga']
tupla_suco = ('laranja', 'uva', 'abacaxi', 'manga')

lista_refrigerantes = ['coca', 'guaraná', 'laranja', 'uva']

# não existe cmp no python 3
# pegou a ordem alfabética "u"
# print(max(lista_suco))
# # pegou a ordem alfabética "a"
# print(min(lista_suco))

# print(len(lista_suco))

# print(type(list(tupla_suco)))

lista_suco2 = ['laranja', 'uva', 'abacaxi', 'manga']
# conta quantas vezes tem um elemento
# print(lista_suco2.count('abacaxi'))

lista_suco.extend(lista_refrigerantes)
print(lista_suco)


list3 = lista_suco + lista_suco2

# print(list3)
# # mostrar o que foi excluído, nesse caso "laranja"
# print(list3.pop(4))
# print(list3)
