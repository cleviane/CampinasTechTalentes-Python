
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)               # Prints the complete tuple
print(tuple[0] )           # Prints first element of the tuple
print(tuple[1:3] )         # Prints elements of the tuple starting from 2nd till 3rd 
print(tuple[2:])           # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)       # Prints the contents of the tuple twice
print(tuple + tinytuple)   # Prints concatenated tuples

#  a tuple não será alterada
tuple(0) = "hahaha"

# bem parecido com listas usa-se ()
# para ler melhor
# não muda o valor dela, parecido com costante
