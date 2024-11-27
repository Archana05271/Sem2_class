#class 
class Books:
    library_name = 'ABC Publishers'
#constructor
    def __init__(self, name, author):
        self.name = name#instance variables
        self.author = author

    def show(self):
        print(f"Book Name: {self.name}, Author name: {self.author}")
#object
book1 = Books("Ram c/o anandhi", "Akhil")
book1.show()

book2 = Books("Ugly Love", "Colleen Hoover")
book2.show()

#default constructor
class Books:
    library_name = 'ABC Publishers'

    def __init__(self):
        self.name = "Ugly Love"
        self.author = "Colleen Hoover"

    def show(self):
        print(f"Book Name: {self.name}, Author name: {self.author}")
book=Books()
book.show()
#non parameterised

class Books:
    library_name = 'ABC Publishers'
#constructor
    def __init__(self, name, age=38,publishing =893):
        self.name = name#instance variables
        self.age = age
        self.publishing=publishing

    def show(self):
        print(self.name,self.age,self.publishing)
#object
book1 = Books("Ram c/o anandhi")
book1.show()

