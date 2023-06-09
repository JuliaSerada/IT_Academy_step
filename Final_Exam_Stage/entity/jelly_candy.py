from Final_Exam_Stage.entity.sweets import Sweets


class JellyCandy(Sweets):
    def __init__(self, color="red", weight=0, price=0):
        super().__init__(price)
        self.__color = color
        self.__weight = weight

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self.__color = color

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight

    def __str__(self):
        return (f"Jelly candy: color = {self.__color}, "
                f"weight = {self.__weight}, "
                f"price = ${self.price}.")
