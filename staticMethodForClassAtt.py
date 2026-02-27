class Test:
    __secret = 100

    @staticmethod
    def show():
        Test.__secret+=1
        print(Test.__secret)

a=Test()
a.show()

b=Test()
b.show()

Test.show()
a.show()

# When to use static method
# 1. when function not use any instance attribute
# 2. static functions don't have any parameter like self,cls,other parameter.
# 3. they can access class atribute using class name

