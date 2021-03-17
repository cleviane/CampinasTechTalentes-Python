nome = "Clevi"
pessoa = "Outra Pessoa"
ispessoa = True

if pessoa == "Outra Pessoa":
    print("É aluno")
    if ispessoa == True:
       print(f"Olá {nome}!")
    else:
        print("Olá alguém")
        
elif pessoa == "Aluno":
    print("É Aluno")
    if ispessoa:
        print(f"Olá {nome}")
    else:
        print("Olá outra pessoa")
    
elif pessoa == "Outra Pessoa":
    print("Olá Outra Pessoa!")
    