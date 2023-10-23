class Fruit:
    def __init__(self, fruit_type, price, color):
        self.fruit_type = fruit_type
        self.price = price
        self.color = color

    def show(self):
        print(f"The fruit of my choice is a ripe {self.color} {self.fruit_type} and is priced at {self.price}")


fruit = Fruit("Banana", 20, "yellow")
fruit.show()