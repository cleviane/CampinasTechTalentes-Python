
from Employee import Employee
from Pessoa import Pessoa
# Criando objetos
# empregado = Employee("Jeff", 10000000.00)
# print(f"O nome do empregado é {empregado.name} ")
# print(f"E o seu salário é {empregado.salary} ")

# empregada = Employee("Paula", 100000000.00)
# print(f"O nome do empregada é {empregada.name} ")
# print(f"E o seu salário é {empregada.salary} ")

#Solicitando valores no terminal
nome = input("Coloque o nome do Empregado \n")
salario = float(input("Coloque o seu salário\n"))
# #Criando objeto Employee
# novo_empregado = Employee(name=nome, salary=salario)
# print(f"O nome do empregada é {novo_empregado.name} ")
# print(f"E o seu salário é {novo_empregado.salary} ")
# especificar o nome do argumento (parametro) ajuda a classe determinar os parametros
# pessoa = Pessoa(salario=0, nome="Je")
# print(f"O nome é: {pessoa.nome}")
# Criando objetos
# empregado = Employee("Jeff", 10000000.00)
# print(f"O nome do empregado é {empregado.name} ")
# print(f"E o seu salário é {empregado.salary} ")


# - The ** getattr(obj, name[, default]) ** − to access the attribute of object.
# - The ** hasattr(obj, name) ** − to check if an attribute exists or not.
# - The ** setattr(obj, name, value) ** − to set an attribute. If attribute does not exist, then it would be created.
# - The ** delattr(obj, name) ** − to delete an attribute.

# ```
# hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
# getattr(emp1, 'age')    # Returns value of 'age' attribute
# setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
# delattr(empl, 'age')    # Delete attribute 'age'

emp = Employee("Clevi", 10)#criando objeto
print(emp.name)#pegando o valor do atributo/campo
print(getattr(emp,'name'))#pegando o valor do atributo/campo
print(hasattr(emp,'name'))# verificando o valor do atributo/campo existe
setattr(emp,'name',"Cleviane")#atribuir valor para o campo nome
print(emp.name)#conferindo a mudança
delattr(emp,'name')#exclui o atributo do objeto (da intância)
print(emp.name)#conferindo a mudança

