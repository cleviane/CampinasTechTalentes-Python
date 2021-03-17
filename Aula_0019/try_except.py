try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Erro: Fofinho, não pode escrever o arquivinho.")
else:
   print("Fofinho, escreveu o arquivinho viu?!")
   fh.close()
