class FruitMarket:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = {}

    def add_fruit(self, fruit_name, quantity, price_per_unit):
        if fruit_name in self.inventory:
            self.inventory[fruit_name]['quantity'] += quantity
        else:
            self.inventory[fruit_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}

    def remove_fruit(self, fruit_name, quantity):
        if fruit_name in self.inventory:
            if self.inventory[fruit_name]['quantity'] >= quantity:
                self.inventory[fruit_name]['quantity'] -= quantity
            else:
                raise ValueError("Not enough fruit in stock.")
        else:
            raise ValueError("Fruit not found in inventory.")

    def get_inventory(self):
        return self.inventory

    def get_total_value(self):
        total_value = 0
        for fruit, details in self.inventory.items():
            total_value += details['quantity'] * details['price_per_unit']
        return total_value

market = FruitMarket("Fruit Market", "Jl. Buah")
market.add_fruit("Apple", 10, 2000)
market.add_fruit("Orange", 5, 1500)
market.remove_fruit("Apple", 3)
print(market.get_inventory())
print(market.get_total_value())


