class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    def get_address(self):
        return f"{self.__city}, {self.__state}, {self.__country}"

class Employee:
    def __init__(self, name, salary, age, address):
        self.name = name
        self.salary = salary
        self.age = age
        self.address = address

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address.get_address()}"

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, age, address, hours_worked):
        super().__init__(name, salary, age, address)
        self.hours_worked = hours_worked

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address.get_address()}, Hours Worked: {self.hours_worked}"

class Contractor(Employee):
    def __init__(self, name, salary, age, address):
        print("Contractor",name, salary, age, address)
        super().__init__(name, salary, age, address)  # Initialize the Employee part

    def get_details(self):
        super().get_details()
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address.get_address()}"

class ContractorPartTimeEmployee(PartTimeEmployee, Contractor):
    def __init__(self, name, salary, age, address, hours_worked):
        # super().__init__(name, salary, age, address, hours_worked)
        PartTimeEmployee.__init__(self, name, salary, age, address, hours_worked)
        Contractor.__init__(self, name, salary, age, address)


cpt = ContractorPartTimeEmployee("John Doe", 10000, 30, Address("New York", "NY", "USA"), 5)
print(cpt.get_details())
print(Contractor.get_details(cpt))

# c = Contractor("John Doe",100000000,23,Address("New York", "NY", "USA"))
# print(c.get_details())

# pte = PartTimeEmployee("John Doe", 10000, 30, Address("New York", "NY", "USA"), 5)

# print(pte.get_details())
# print(c.get_details())