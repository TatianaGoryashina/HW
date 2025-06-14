class User:

    def __init__(self, name, lastname):
        self.first_name = name
        self.last_name = lastname

    def say_name(self):
        print(f"Мое имя {self.first_name}")

    def say_last_name(self):
        print(f"Моя фамилия {self.last_name}")

    def say_full_name(self):
        print(f"Меня зовут {self.first_name}, {self.last_name}")
