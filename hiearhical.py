class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name : ",self.name,"\nAge : ",self.age)


class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("ID : ",self.Id)

class Manager(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def displayManager(self):
        self.displayPerson()
        print("Salary : ",self.salary)
emp1=Employee("Kanish",27,3412)
emp2=Manager("Ragu",35,25000)
emp1.displayEmployee()
emp2.displayManager()
