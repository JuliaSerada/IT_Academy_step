class Laptop:
    def __init__(self, brand="no name", model="no name", price=0, number=0):
        self.brand = brand
        self.model = model
        self.price = price
        self.number = number

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Laptop: {self.brand}, model: {self.model}, price = ${self.price}, " \
               f"number = {self.number}."

    def __str__(self) -> str:
        return f"Computer: " \
               f"brand = {self.get_brand()}, " \
               f"model = {self.get_model()}, " \
               f"price = {self.get_price()} BYN"


if __name__ == "__main__":
    laptop1 = Laptop("Apple")
    laptop2 = Laptop("Acer")
    laptop3 = Laptop("HP")
    laptop4 = Laptop("Lenovo")
    laptop5 = Laptop("Asus")


msg = f"""Statistic result:
    Total amount: {Manager.total_amount(laptops)}
    Computer with Max price: {Manager.max_price(laptops)} 
    Computer with Min price: {Manager.min_price(laptops)}
    """
    print(msg)


@staticmethod
    def total_amount(ls):
        total_amount = 0
        for item in ls:
            total_amount += item.get_price()
        return total_amount

    @staticmethod
    def max_price(ls):
        max_laptop = ls[0]
        for item in ls:
            if item.get_price() > max_laptop.get_price():
                max_laptop = item
        return max_laptop

    @staticmethod
    def min_price(ls):
        min_laptop = ls[0]
        for item in ls:
            if item.get_price() < min_laptop.get_price():
                min_laptop = item
        return min_laptop

laptop1 = Laptop("Apple", "Macbook Air Pro 14", 1600, 55),
    laptop2 = Laptop("Acer", "Acer Chromebook Spin 714", 679, 22)
    laptop3 = Laptop("HP", "HP ENVY x360", 1300, 20)
    laptop4 = Laptop("Lenovo", "Lenovo Yoga 9i 14", 1234, 32)
    laptop5 = Laptop("Asus", "ASUS ROG Zephyrus G14", 1050, 28)

    ls = (laptop1, laptop2, laptop3, laptop4, laptop5)

[Laptop(brand="Apple", model="Macbook Air Pro 14", price=1600, number=55),
          Laptop(brand="Acer", model="Acer Chromebook Spin 714", price=679, number=22),
          Laptop(brand="HP", model="HP ENVY x360", price=1300, number=20)]


class Laptop:
    def __init__(self, brand="no name", model="no name", price=0, number=0):
        super().__init__()
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
        return f"Laptop: {self.get_brand}, model: {self.get_model}, price = ${self.get_price}, " \
               f"number = {self.get_number}."

