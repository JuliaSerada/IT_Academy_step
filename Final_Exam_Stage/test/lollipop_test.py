import unittest
from Final_Exam_Stage.entity.lollipop import Lollipop


class LollipopTest(unittest.TestCase):
    def test_lollipop_default_constructor(self):
        lollipop = Lollipop()
        expected_flavor = "apple"
        expected_weight = 0
        expected_price = 0

        self.assertEqual(expected_flavor, lollipop.flavor)
        self.assertEqual(expected_weight, lollipop.weight)
        self.assertEqual(expected_price, lollipop.price)

    def test_lollipop_constructor_with_args(self):
        expected_flavor = "apple"
        expected_weight = 15.0
        expected_price = 7

        lollipop = Lollipop(expected_flavor, expected_weight, expected_price)

        self.assertEqual(expected_flavor, lollipop.flavor)
        self.assertEqual(expected_weight, lollipop.weight)
        self.assertEqual(expected_price, lollipop.price)

    def test_negative_lollipop_with_invalid_flavor(self):
        flavor = "orange"
        expected = "orange"

        lollipop = Lollipop(flavor=flavor)

        self.assertEqual(expected, lollipop.flavor)

    def test_negative_lollipop_weight(self):
        weight = -20
        expected = -20

        lollipop = Lollipop(weight=weight)

        self.assertEqual(expected, lollipop.weight)

    def test_zero_lollipop_weight(self):
        weight = 0
        expected = 0

        lollipop = Lollipop(weight=weight)

        self.assertEqual(expected, lollipop.weight)

    def test_zero_lollipop_price(self):
        price = 0
        expected = 0

        lollipop = Lollipop(price=price)

        self.assertEqual(expected, lollipop.price)

    def test_flavor_property_negative(self):
        lollipop = Lollipop()
        expected = lollipop.flavor
        lollipop.flavor = "apple"
        self.assertEqual(expected, lollipop.flavor)

    def test_flavor_property_positive(self):
        lollipop = Lollipop()
        expected = lollipop.flavor
        lollipop.flavor = "apple"
        self.assertEqual(expected, lollipop.flavor)

    def test_weight_property_with_zero(self):
        lollipop = Lollipop()
        expected = lollipop.weight
        lollipop.weight = 0
        self.assertEqual(expected, lollipop.weight)

    def test_weight_property_negative(self):
        lollipop = Lollipop()
        expected = lollipop.weight
        lollipop.weight = -100
        self.assertEqual(expected, lollipop.weight)

    def test_weight_property_positive(self):
        lollipop = Lollipop()
        expected = 20
        lollipop.weight = 20
        self.assertEqual(expected, lollipop.weight)


if __name__ == "__main__":
    unittest.main()
