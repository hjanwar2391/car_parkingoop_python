class Car:
    def __init__(self, license_plate, make, model):
        self.license_plate = license_plate
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model} (License Plate: {self.license_plate})"


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_cars = []

    def park_car(self, car):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars.append(car)
            print(f"{car} has been parked.")
        else:
            print("Parking lot is full. Cannot park the car.")

    def remove_car(self, license_plate):
        for car in self.parked_cars:
            if car.license_plate == license_plate:
                self.parked_cars.remove(car)
                print(f"{car} has been removed from the parking lot.")
                return
        print(f"Car with license plate {license_plate} is not found in the parking lot.")

    def list_parked_cars(self):
        if not self.parked_cars:
            print("Parking lot is empty.")
        else:
            print("Cars parked in the parking lot:")
            for car in self.parked_cars:
                print(car)


# Example usage:

# Create a parking lot with a capacity of 3
parking_lot = ParkingLot(3)

# Create some cars
car1 = Car("ABC123", "Toyota", "Camry")
car2 = Car("XYZ789", "Honda", "Civic")
car3 = Car("DEF456", "Ford", "Focus")
car4 = Car("GHI789", "Tesla", "Model 3")

# Park cars in the parking lot
parking_lot.park_car(car1)
parking_lot.park_car(car2)
parking_lot.park_car(car3)
parking_lot.park_car(car4)  # This car will not be parked because the parking lot is full

# List parked cars
# parking_lot.list_parked_cars()

# Remove a car from the parking lot
parking_lot.remove_car("XYZ789")

# List parked cars again
parking_lot.list_parked_cars()
