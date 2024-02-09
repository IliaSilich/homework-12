class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int = 1) -> None:
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                break
        else:
            self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product: Product, quantity: int = 1) -> None:
        for item in self.items:
            if item['product'] == product:
                item['quantity'] -= quantity
                if item['quantity'] <= 0:
                    self.items.remove(item)
                break

    def get_total(self) -> float:
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total


product1 = Product(name="Laptop", price=1200.0, description="High-performance laptop")
product2 = Product(name="Mouse", price=30.0, description="Wireless mouse")

cart = Cart()
cart.add_item(product1, quantity=2)
cart.add_item(product2, quantity=1)

print(f"Total cost in the cart: ${cart.get_total()}")

cart.remove_item(product1, quantity=1)

print(f"Total cost in the cart: ${cart.get_total()}")
