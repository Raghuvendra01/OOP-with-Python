class Car:
    def __init__(self,brand,model):
        self.__model=model;
        self.__brand=brand;

    @property
    def Model_information(self):
        return self.__model

New_car=Car("Range Rover", "sport")
print(New_car.Model_information)

# Property decorator is used when we don't want to change
# value after initializing it once. And water if propert function
# name is, it can be used as propert with object to access the attribute
