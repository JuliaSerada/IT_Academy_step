from Final_Exam_Stage.entity.sweets import Sweets


class NewYearGift:
    def __init__(self, sweets=None):
        if not sweets:
            self.__sweets = []
        else:
            self.__sweets = sweets

    @property
    def size(self):
        return len(self.__sweets)

    def get_sweet(self, index):
        if isinstance(index, int) and index >= 0 and index < self.size:
            return self.__sweets[index]

    def add(self, sweet):
        if isinstance(sweet, Sweets):
            self.__sweets.append(sweet)

    def __str__(self):
        msg = "List of sweets:"
        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__sweets[i])

        return msg
