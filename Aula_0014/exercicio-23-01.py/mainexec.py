from Contato import Contato

lista = []
lista_opcoes = ["", "1- Lista de contatos", "2- Excluir contato",
               "3- Inserir contato", "4- Sair"]
# lista vazia
# fazer 3 inputs para a pessoa escrever
# instanciar tem que passar o objeto e os atributos
# usando lista .append no objeto
# lista .append 
nome_usuario = input("Digite o nome do usuário do sistema: ")

while True:  # enquanto for verdade ficará executando o programa
    print(f"Olá {nome_usuario}, selecione as opções abaixo: ")
    for opcao in lista_opcoes:  # Lista as opções na tela do usuário
        print(opcao)    
    opcao_selecionada = int(input(""))
    
    if opcao_selecionada == 1:
        for contato in lista:
            print(f"O contato foi adicionado {contato.nome} na agenda.")
   
    elif opcao_selecionada == 2: 
        while True: 
            indice = 0 
            for item in lista:
                print(f"{indice} - {item.nome}")
                indice += 1
            print(f"Selecione {indice} para sair...")
            indice__selecionado = input("Qual desses contatos você quer excluir? (Digite um número)\n")

            if indice__selecionado.isnumeric():
                indice__selecionado_convertido = int(indice__selecionado)
                
                if indice__selecionado_convertido in range(0, indice):
                    print("Apagando...")
                    item_selecionado = lista.pop(
                        indice__selecionado_convertido) 
                    print(f"Seu contato {item_selecionado.nome} foi removido!")
                    break

                elif indice__selecionado_convertido == indice:
                    break
                else:

                    print("Não existe essa opção")
            else: 
                print("Opção incorreta ou inexistente")

    elif opcao_selecionada == 3:  
        nome = input("Digite o nome do contato:\n")
        telefone = input("Digite o número de telefone do contato:\n")
        endereco = input("Digite o endereço do contato:\n")
        
        contato = Contato(nome, telefone, endereco)
        lista.append(contato)
        
        print("Contato inserido!")
        
    elif opcao_selecionada == 4: 
        print("Você saiu do sistema!")
        break

    # Se o usuário não selecionou nenhuma das opções existentes então avise que não existe a opção
    elif list_opcoes not in (1, 2, 3, 4):

        print("Opção errada ou inexistente")
# contato= Contato(nome, telefone, endereco)
# lista.append(contato)

# for contato in lista:
#      print("Dados do Contato!!")
#      print(f"Nome: {contato.nome}\nTelefone: {telefone}\nEndereço: {endereco}")
