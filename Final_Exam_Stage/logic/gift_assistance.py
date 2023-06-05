from Final_Exam_Stage.container.new_year_gift import NewYearGift
from Final_Exam_Stage.entity.sweets import Sweets
from Final_Exam_Stage.entity.chocolate_candy import ChocolateCandy
from Final_Exam_Stage.entity.jelly_candy import JellyCandy
from Final_Exam_Stage.entity.lollipop import Lollipop


class GiftAssistance:

    @staticmethod
    def calculate_total_price(gift):
        if isinstance(gift, NewYearGift) and gift.size != 0:
            total = 0
            for i in range(gift.size):
                sweet = gift.get_sweet(i)

                if isinstance(sweet, Sweets):
                    total += sweet.price

            return total
        else:
            return 0

    @staticmethod
    def calculate_total_weight(gift):
        if isinstance(gift, NewYearGift) and gift.size != 0:
            total = 0
            for i in range(gift.size):
                sweet = gift.get_sweet(i)

                if isinstance(sweet, Sweets):
                    total += sweet.weight

            return total
        else:
            return 0

    @staticmethod
    def get_max_price():
        ls = [ChocolateCandy(ingredient="nuts", brand="Snickers", weight=95.5, price=15),
              Lollipop(flavor="apple", weight=15.0, price=7),
              JellyCandy(color="red", weight=4.2, price=5.5)]

        max_sweet = ls[0]

        for unit in ls:
            if unit.get_price() > max_sweet.get_price():
                max_sweet = unit

        return max_sweet

    @staticmethod
    def get_min_price():
        ls = [ChocolateCandy(ingredient="nuts", brand="Snickers", weight=95.5, price=15),
              Lollipop(flavor="apple", weight=15.0, price=7),
              JellyCandy(color="red", weight=4.2, price=5.5)]

        min_sweet = ls[0]

        for unit in ls:
            if unit.get_price() < min_sweet.get_price():
                min_sweet = unit

        return min_sweet
