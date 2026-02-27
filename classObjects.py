"""
# class is blueprint for objects
class Car:
    
    #constructor 
    #specific object's attributes it initializes
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    #behaviour of obejects
    def full_name(self):
        return f"{self.brand} {self.model}"

""" 
"""
 inheritance -> by inheriting car class, we have all attributes 
 of Car in Electric_Car 

"""
"""

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size;

    def Allfeatures(self):
        return f"{self.brand}\n{self.model}\n{self.battery_size}"

    
    

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.full_name())

New_electric_car= Electric_Car("Toyota", "Inova", "1000mAh")
print(New_electric_car.Allfeatures())
print(New_electric_car.full_name())

"""

#privatization
class BankAccount:
    def __init__(self,account_no,money):
        self.account_no=account_no
        self.__money=money
        
    # only you can access money using getter function 
    # because money is private attributes    
    def getMoney(self):
        return self.__money
    
New_Bank_Account=BankAccount(823810001,5000)
print(New_Bank_Account.getMoney())


