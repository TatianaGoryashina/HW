class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.phone_number = number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"
