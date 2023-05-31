from Final_Exam_Stage.container.new_year_gift import NewYearGift
from Final_Exam_Stage.entity.sweets import Sweets


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
