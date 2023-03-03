from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def get_specs(self):
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class Sedan(Car):
    def get_specs(self):
        return "This is a Sedan car with 4 doors and a fuel-efficient engine."

class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()

class SUV(Car):
    def get_specs(self):
        return "This is an SUV car with 4-wheel drive and a spacious interior."

sedan_factory = SedanFactory()
sedan = sedan_factory.create_car()
print(sedan.get_specs())  

suv_factory = SUVFactory()
suv = suv_factory.create_car()
print(suv.get_specs()) 