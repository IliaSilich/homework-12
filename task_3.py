class Vehicle:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def start() -> None:
        print("The vehicle is starting")


class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        super().__init__(brand, model, color)
        self.doors = doors

    @staticmethod
    def honk() -> None:
        print("The car is honking")


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, color: str, gears: int):
        super().__init__(brand, model, color)
        self.gears = gears

    @staticmethod
    def pedal() -> None:
        print("The bike is pedaling")


class Plane(Vehicle):
    def __init__(self, brand: str, model: str, color: str, wingspan: float):
        super().__init__(brand, model, color)
        self.wingspan = wingspan

    @staticmethod
    def fly() -> None:
        print("The plane is flying")


car = Car(brand="Toyota", model="Camry", color="Blue", doors=4)
car.start()
car.honk()

bike = Bike(brand="Kawasaki", model="Z900", color="Black", gears=6)
bike.start()
bike.pedal()

plane = Plane(brand="Boeing", model="747", color="White", wingspan=68.4)
plane.start()
plane.fly()
