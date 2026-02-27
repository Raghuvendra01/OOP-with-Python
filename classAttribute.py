# class Car:
#     totalCar = 0

#     def __init__(self):
#         """ it creates new instance attribute 
#             using present class attribute value
#              by adding 1 in that 
#         """
#         self.totalCar += 1

# a = Car() #a.totalCar = Car.totalCar+1
# b = Car() #b.totalCar = Car.totalCar+1
# c = Car() #c.totalCar = Car.totalCar+1

# print(Car.totalCar) #output 0
# print(a.totalCar) #output 1
# print(b.totalCar) #output 1
# print(c.totalCar) #output 1

class Student:
    college_name="ABC college"
    name="anonymous" 

    def __init__(self,marks):
        self.marks=marks
    
    #now we have only one constructor this 
    #this constructor replaces above constructor
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks


s1=Student("Raghu",84)
print(s1.name," ",s1.marks)

#python doesn't support parameter overloading 
# s2=Student(90)
# print(s2.name," ",s2.marks)