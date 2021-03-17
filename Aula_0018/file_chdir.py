import os

nome_diretorio = "test"
# Changing a directory to "/home/newdir"
os.chdir(f"C:\CursoPython\Aula_18\{nome_diretorio}")

if os.getcwd() == f"C:\CursoPython\Aula_18\{nome_diretorio}":
    print("beleza!!!!")

print(os.getcwd())
