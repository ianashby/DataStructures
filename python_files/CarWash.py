class CarWash:
    def __init__(self):
        self.queue = []

    def add_car(self, car):
        # Your code here.
        pass

    def remove_car(self):
        return self.queue.pop(0)

    def length(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


# Test case 1:
car_wash = CarWash()
car_wash.add_car('BMW')
car_wash.add_car('Audi')
car_wash.add_car('Mercedes')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche')
car_wash.add_car('Lamborghini')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche')
car_wash.add_car('Lamborghini')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche') # This car should not be added.
car_wash.add_car('Lamborghini') # This car should not be added.

# Test case 2:
car_wash = CarWash()
car_wash.add_car('BMW')
car_wash.add_car('Audi')
car_wash.add_car('Mercedes')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche')
car_wash.add_car('Lamborghini')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche')
car_wash.add_car('Lamborghini')
car_wash.add_car('Ferrari')
car_wash.add_car('Porsche 1') # This car should not be added.
car_wash.remove_car()
car_wash.remove_car()
car_wash.add_car('Porsche 2') # This car should be added.
print(car_wash)