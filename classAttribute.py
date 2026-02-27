class Car:
    totalCar = 0

    def __init__(self):
        """ it creates new instance attribute 
            using present class attribute value
             by adding 1 in that 
        """
        self.totalCar += 1

a = Car() #a.totalCar = Car.totalCar+1
b = Car() #b.totalCar = Car.totalCar+1
c = Car() #c.totalCar = Car.totalCar+1

print(Car.totalCar) #output 0
print(a.totalCar) #output 1
print(b.totalCar) #output 1
print(c.totalCar) #output 1