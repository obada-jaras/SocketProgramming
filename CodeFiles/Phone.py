class Phone:
    name = ''
    price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name + ',' + self.price
