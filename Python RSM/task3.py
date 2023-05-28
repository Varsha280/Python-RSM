class Vehicle():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Start")
    
    def stop(self):
        print("Stop")

    def display_info(self):
        print("Vehicle Information")
        print("Ma:", self.make)
        print("Mo:", self.model)
        print("Y:", self.year)

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, num_axles):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.num_axles = num_axles

myCar = Car("Mercedes", "Benz A-class", 2022, 4, "Diesel")
myMotorcycle = Motorcycle("Vespa", "Vespa300", 2009, 120)
myTruck = Truck("Tata", "Tacoma", 2021, "1000 Kg", 2)

myCar.start()
myCar.display_info()
myCar.stop()

print()

myMotorcycle.start()
myMotorcycle.display_info()
myMotorcycle.stop()

print()

myTruck.start()
myTruck.display_info()
myTruck.stop()


