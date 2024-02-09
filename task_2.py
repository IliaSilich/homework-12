class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self) -> str:
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, position: str, salary: float):
        super().__init__(name, position, salary)
        self.subordinates = []

    def get_info(self) -> str:
        info = super().get_info()
        subordinate_count = len(self.subordinates)
        return f"{info}, Subordinates: {subordinate_count}"

    def add_subordinate(self, subordinate: Employee):
        if subordinate not in self.subordinates:
            self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate: Employee):
        if subordinate in self.subordinates:
            self.subordinates.remove(subordinate)


employee1 = Employee(name="John Doe", position="Developer", salary=50000.0)
employee2 = Employee(name="Jane Doe", position="Designer", salary=55000.0)

manager = Manager(name="Alice Manager", position="Team Lead", salary=70000.0)
manager.add_subordinate(employee1)
manager.add_subordinate(employee2)

print(manager.get_info())
print(employee1.get_info())

manager.remove_subordinate(employee1)

print(manager.get_info())
