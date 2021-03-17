# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# finally:  # Sempre ser executado, não importando se deu erro ou não
#    print("Error: can\'t find file or read data")
#    fh.close()

try:
   fh = open("testfile", "w")
   try:
       fh.write("This is my test file for exception handling!!")
   finally: 
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")
