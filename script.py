from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass
    
    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    def engine(self):
        return 'car engine'
    
    def wheels(self):
        return 4

class Bike(Vehicle):
    def engine(self):
        return 'bike engine'
    
    def wheels(self):
        return 2

class Truck(Vehicle):
    def engine(self):
        return 'truck engine'
    
    def wheels(self):
        return 18

c = Car()
print(c.engine())
print(c.wheels())