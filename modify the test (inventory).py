class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the prodID:")
        self.name=input("Enter the prodName:")
        self.count=int(input("Enter the prodCount:"))
    def displayInventoryInfo(self):
        print("PROD_ID = ",self.id,"\nPROD_Name = ",self.name,"\nPROD_Count = ",self.count)

class Perks(Inventory):
    def getDetails(self):
        self.getInventoryInfo()
        self.price=int(input("Enter the price: "))
    def displayInfo(self):
        self.displayInventoryInfo()
        print("Price = ",self.price)

p=Perks()
p.getDetails()
p.displayInfo()
