from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"