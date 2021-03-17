def changeme(mylist):
   "This changes a passed list into this function"
   mylist.append([1, 2, 3, 4])
   print("Valores dentro da função: ", mylist)
   print(hex(id(mylist)))

   return

# Now you can call changeme function
minha_lista = [10, 20, 30]
changeme(minha_lista)
print("Valores fora da função: ", minha_lista)
print(hex(id(minha_lista)))
