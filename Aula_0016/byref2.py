

def changeme(mylist):
   "This changes a passed list into this function"
   mylist = [1, 2, 3, 4]  # This would assig new reference in mylist
   print("Valores dentra da função: ", mylist)
   print(hex(id(mylist)))

   return


# Now you can call changeme function
minha_lista = [10, 20, 30]
changeme(minha_lista)
print("Valores fora da função: ", minha_lista)
print(hex(id(minha_lista))) # endereço de memória
