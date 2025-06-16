
# Both method does not allow self
# Class method is called with cls as args without object only helpful in accessing class variable
# Static method is initated without object
# if both are defined with same fn name then last method of class is called

class Person:
    PI = 3.14

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_PI(cls):
        print("Class method is explictilty called")
        return cls.PI
    
    @staticmethod
    def get_static_PI():
        print("Static method called")
        return 3.14
    
    def get_details(self):
        print("Pi From object method")
        return self.PI


print(Person.get_static_PI())

p1 = Person("A", 12)
print(p1.get_details())

print(Person.get_PI())