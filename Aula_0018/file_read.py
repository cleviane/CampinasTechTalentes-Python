# Open a file
fo = open("foo.txt", "r+")
# read leitura de uma vez
str = fo.readline() #readline leitura por linha
print("Read String is : ", str)

# Close opened file
fo.close()
