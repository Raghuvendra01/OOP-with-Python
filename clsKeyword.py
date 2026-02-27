# why class method when we have Static Method ? 
# we only can access class method when it is hard coded
# like Animal.category it causes problem in inheritance
"""
class Animal:
    category = "Living Being"

    @staticmethod
    def show():
        print(Animal.category)  # Class name is hardcoded

class Dog(Animal):
    category = "Canine"

Dog.show()  # "Living Being" output which is wrong.

"""
class Animal:
    category = "Living Being"

    @classmethod
    def show(cls):
        print(cls.category)  # cls = which class show() calls, it prints that category

class Dog(Animal):
    category = "Canine"

Dog.show()   # "Canine" ✅ — Right!
Animal.show() # "Living Being" ✅ — Right!
