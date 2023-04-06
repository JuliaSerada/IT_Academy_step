class Human:
    def __init__(self, first_name="no name", surname="no name", age=1, alive=True):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__alive = alive

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 < age <= 100:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def is_adult(self):
        return self.__age >= 18

    def __str__(self):
        return f"{self.__first_name}, {self.__surname}: age = {self.__age}." \
               f" Is alive? - {self.is_alive}."
