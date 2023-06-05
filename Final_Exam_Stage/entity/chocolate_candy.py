from Final_Exam_Stage.entity.sweets import Sweets


class ChocolateCandy(Sweets):
    def __init__(self, ingredient="nuts", brand="Snickers", weight=0, price=0):
        super().__init__(price)
        self.__ingredient = ingredient
        self.__brand = brand
        self.__weight = weight

    @property
    def ingredient(self):
        return self.__ingredient

    @property
    def brand(self):
        return self.__brand

    @property
    def weight(self):
        return self.__weight

    @ingredient.setter
    def ingredient(self, ingredient):
        if isinstance(ingredient, str):
            self.__ingredient = ingredient

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight

    def __str__(self):
        return (f"Chocolate candy: ingredient = {self.__ingredient}, "
                f"brand = {self.__brand}, "
                f"weight = {self.__weight}, "
                f"price = ${self.price}.")
