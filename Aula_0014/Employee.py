class Employee:
#'Common base class for all employees'
  empCount = 0

def __init__(self, name, salary):
    self.nome = name
    self.salary = salary
    Employee.empCount += 1

def display_count(self):
    print("Total Employee %d" % Employee.empCount)

def display_employee(self):
    print("Name : ", self.name,  ", Salary: ", self.salary)

# seleciona o código + shift + tab para identar 
