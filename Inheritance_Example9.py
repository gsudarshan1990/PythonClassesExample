class Pizza:
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # Scale from 1 to 5


# Add the subclasses below this line
class PizzaMargherita(Pizza):

    def __init__(self, size1, toppings1, price1, rating1, extra_cheese):
        super().__init__(size1, toppings1, price1, rating1)
        self.has_extra_cheese = extra_cheese


class PizzaMarinara(Pizza):
    def __init__(self, size, toppings, price, rating, extra_basil):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_basil = extra_basil


margherita = PizzaMargherita("small", "garlic", 10, "5", True)
marinara = PizzaMarinara("medium", "jalapeno", 9, "5", False)