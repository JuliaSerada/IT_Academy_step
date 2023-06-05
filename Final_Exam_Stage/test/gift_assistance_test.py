import unittest
from Final_Exam_Stage.container.new_year_gift import NewYearGift
from Final_Exam_Stage.entity.sweets import Sweets
from Final_Exam_Stage.logic.gift_assistance import GiftAssistance


class GiftAssistanceTest(unittest.TestCase):
    def test_different_type(self):
        gift = "string"
        expected = 0

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    def test_empty_gift(self):
        gift = NewYearGift()
        expected = 0

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    def test_gift_with_None(self):
        gift = None
        expected = 0

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    def test_gift_positive(self):
        sweet1 = Sweets(7)
        sweet2 = Sweets(12)
        sweet3 = Sweets(7)

        gift = NewYearGift()
        gift.add(sweet1)
        gift.add(sweet2)
        gift.add(sweet3)

        expected = 26

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    def test_gift_with_one_product(self):
        sweet = Sweets(5)

        gift = NewYearGift()
        gift.add(sweet)

        expected = sweet.price

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    def test_gift_with_sweets_positive(self):
        sweet1 = Sweets(7)
        sweet2 = Sweets(12)
        sweet3 = Sweets(7)

        gift = NewYearGift()
        gift.add(sweet1)
        gift.add("string")
        gift.add(sweet2)
        gift.add(sweet3)
        gift.add(5)

        expected = 26

        actual = GiftAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
