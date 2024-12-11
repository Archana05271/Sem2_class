class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployee(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Manager(Employee):
    def __init__(self,name,age,eid):
       Employee.__init__(self,name,age)
       self.eid=eid
    def displayManager(self):
        self.displayEmployee()
        print("Eid:",self.eid)
        
class Developer(Employee):
    def __init__(self,name,age,dept):
       Employee.__init__(self,name,age)
       self.dept=dept
    def displayDeveloper(self):
        self.displayEmployee()
        print("Department:",self.dept)
class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamLeader(self):
        print("TeamSize:",self.teamsize)
name=input("Enter the name:")
age=int(input("Enter the age:"))
eid=int(input("Enter the Eid:"))
dept=input("Enter the department:")
teamsize=int(input("Enter the teamsize:"))
per=TeamLeader(name,age,eid,dept,teamsize)
per.displayEmployee()
per.displayManager()
per.displayDeveloper()
per.displayTeamLeader()
    
        
