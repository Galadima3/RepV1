class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class Toyota(Car):
    def __init__(self, make, model, year, price):
        super().__init__(make, model, year)
        self.price = price
                
car = Toyota('Toyota', 'Camry', 2015, 2500)
print(car)