class Laptop:
    def __init__(self, brand="no name", model="no name", price=0, number=0):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__number = number

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_number(self):
        return self.__number

    def __str__(self):
        return f"Laptop: {self.__brand}, model: {self.__model}, price = ${self.__price}, " \
               f"number = {self.__number}."
