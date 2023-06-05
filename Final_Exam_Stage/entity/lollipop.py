from Final_Exam_Stage.entity.sweets import Sweets


class Lollipop(Sweets):
    def __init__(self, flavor="apple", weight=0, price=0):
        super().__init__(price)
        self.__flavor = flavor
        self.__weight = weight

    @property
    def flavor(self):
        return self.__flavor

    @property
    def weight(self):
        return self.__weight

    @flavor.setter
    def flavor(self, flavor):
        if isinstance(flavor, str):
            self.__flavor = flavor

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight

    def __str__(self):
        return (f"Lollipop: flavor = {self.__flavor}, "
                f"weight = {self.__weight}, "
                f"price = ${self.price}.")
