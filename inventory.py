class Inventory:
    def __init__(self,prodID,prodName,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print(f"Product ID = {self.prodID}")
        print(f"Product Name = {self.prodName}")
        print(f"Product Count = {self.prodCount}")

prod=Inventory(1235,"Blender",5)
prod.display()
