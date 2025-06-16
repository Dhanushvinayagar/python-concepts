from typing import override


class Address:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

class Employee:
    def __init__(self, name, salary, age, address):
        self.__name = name
        self.__salary = salary
        self.__age = age
        self.__address = address

    def get_address(self):
        return f"{self.__address.city}, {self.__address.state}, {self.__address.country}"
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def get_age(self):
        return self.__age

    def get_employee_details(self):
        return f"Name: {self.get_name()}, Age: {self.get_age()}, Salary: {self.get_salary()}, Address: {self.get_address()}"

class Manager(Employee):
    def __init__(self, name, salary, age, address, department):
        super().__init__(name, salary, age, address)
        self.department = department

    def get_employee_details(self):
        return super().get_employee_details() + f", Department: {self.department}"
    

e = Employee("John", 50000, 30, Address("New York", "NY", "USA"))
m = Manager("John Doe", 50000, 30, Address("New York", "NY", "USA"), "IT")

print(m.get_employee_details())
print(e.get_name())
print(e.get_employee_details())