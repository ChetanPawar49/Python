from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} (ID: {self.vehicle_id}), Price: ${self.rental_price}/day, {'Available' if self.is_available else 'Rented'}"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, seats):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.seats = seats

    def __str__(self):
        return f"Car: {super().__str__()}, Seats: {self.seats}"

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, engine_capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return f"Bike: {super().__str__()}, Engine: {self.engine_capacity}cc"

class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, load_capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Truck: {super().__str__()}, Load Capacity: {self.load_capacity} tons"

class Customer:
    def __init__(self, name, driver_license_number):
        self.name = name
        self.driver_license_number = driver_license_number
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle, rental_service, rent_date):
        if vehicle.is_available:
            self.rented_vehicles.append({
                'vehicle': vehicle,
                'rent_date': rent_date,
                'return_date': None
            })
            rental_service.rent_vehicle(vehicle)
            print(f"{self.name} has rented {vehicle}")
        else:
            print(f"{vehicle} is not available.")

    def return_vehicle(self, vehicle_id, rental_service, return_date):
        for rental in self.rented_vehicles:
            if rental['vehicle'].vehicle_id == vehicle_id and rental['return_date'] is None:
                rental['return_date'] = return_date
                rental_service.return_vehicle(rental['vehicle'], rental['rent_date'], return_date)
                print(f"{self.name} has returned {rental['vehicle']}")
                return
        print(f"Vehicle with ID {vehicle_id} not found or already returned.")

    def rental_history(self):
        for rental in self.rented_vehicles:
            vehicle = rental['vehicle']
            rent_date = rental['rent_date']
            return_date = rental['return_date'] if rental['return_date'] else "Not returned yet"
            print(f"Rented {vehicle}, Rent Date: {rent_date}, Return Date: {return_date}")

    def __str__(self):
        return f"Customer: {self.name}, License: {self.driver_license_number}"

class RentalService:
    def __init__(self):
        self.vehicles = []
        self.rentals = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def view_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_available]
        if available_vehicles:
            for vehicle in available_vehicles:
                print(vehicle)
        else:
            print("No vehicles available.")

    def rent_vehicle(self, vehicle):
        vehicle.is_available = False
        self.rentals.append(vehicle)

    def return_vehicle(self, vehicle, rent_date, return_date):
        vehicle.is_available = True
        # Calculate rental cost based on days rented
        days_rented = (return_date - rent_date).days
        rental_cost = days_rented * vehicle.rental_price
        print(f"{vehicle} returned. Total cost: ${rental_cost} for {days_rented} days.")

    def __str__(self):
        return f"Rental Service with {len(self.vehicles)} vehicles."

# Example Usage:

# Initialize rental service
rental_service = RentalService()

# Add vehicles to the fleet
car1 = Car("C001", "Toyota", "Camry", 50, 5)
bike1 = Bike("B001", "Yamaha", "R15", 20, 155)
truck1 = Truck("T001", "Ford", "F-150", 100, 3)

rental_service.add_vehicle(car1)
rental_service.add_vehicle(bike1)
rental_service.add_vehicle(truck1)

# Create a customer
customer1 = Customer("John Doe", "DL12345")

# View available vehicles
rental_service.view_available_vehicles()

# Rent a vehicle
rent_date = datetime(2024, 9, 10)
customer1.rent_vehicle(car1, rental_service, rent_date)

# View available vehicles after renting
rental_service.view_available_vehicles()

# Return the vehicle
return_date = datetime(2024, 9, 15)
customer1.return_vehicle("C001", rental_service, return_date)

# View rental history
customer1.rental_history()

# View available vehicles after returning
rental_service.view_available_vehicles()