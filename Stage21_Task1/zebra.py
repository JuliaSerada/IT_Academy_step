class Zebra:
    def __init__(self, name="no name"):
        self.__state = True
        self.__name = name
        # True = black line
        # False = white line

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_stripe(self):
        msg = "black line" if self.__state else "white line"
        self.__state = not self.__state

        return msg

    def __str__(self):
        return f"{self.__name}"
