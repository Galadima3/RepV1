class Person:
    def __init__(self, name, ID) -> None:
        self.name = name
        self.ID = ID

    def greet(self):
        return f"Hi, My name is {self.name} with ID number: {self.ID} and "


class Employee(Person):
    def __init__(self, name, ID, branch) -> None:
        super().__init__(name, ID)
        self.branch = branch

    def greet (self):  
        return super().greet() + f"I work at {self.branch} branch"

employee = Employee ('Mylez', 2050, 'Ikeja')
print(employee.greet())
        
