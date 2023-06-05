import unittest
from Final_Exam_Stage.entity.jelly_candy import JellyCandy


class JellyCandyTest(unittest.TestCase):
    def test_jelly_candy_default_constructor(self):
        jelly_candy = JellyCandy()
        expected_color = "red"
        expected_weight = 0
        expected_price = 0

        self.assertEqual(expected_color, jelly_candy.color)
        self.assertEqual(expected_weight, jelly_candy.weight)
        self.assertEqual(expected_price, jelly_candy.price)

    def test_jelly_candy_constructor_with_args(self):
        expected_color = "red"
        expected_weight = 4.2
        expected_price = 5.5

        jelly_candy = JellyCandy(expected_color, expected_weight, expected_price)

        self.assertEqual(expected_color, jelly_candy.color)
        self.assertEqual(expected_weight, jelly_candy.weight)
        self.assertEqual(expected_price, jelly_candy.price)

    def test_negative_jelly_candy_with_invalid_flavor(self):
        color = "blue"
        expected = "blue"

        jelly_candy = JellyCandy(color=color)

        self.assertEqual(expected, jelly_candy.color)

    def test_negative_jelly_candy_weight(self):
        weight = -50
        expected = -50

        jelly_candy = JellyCandy(weight=weight)

        self.assertEqual(expected, jelly_candy.weight)

    def test_zero_jelly_candy_weight(self):
        weight = 0
        expected = 0

        jelly_candy = JellyCandy(weight=weight)

        self.assertEqual(expected, jelly_candy.weight)

    def test_zero_jelly_candy_price(self):
        price = 0
        expected = 0

        jelly_candy = JellyCandy(price=price)

        self.assertEqual(expected, jelly_candy.price)

    def test_color_property_negative(self):
        jelly_candy = JellyCandy()
        expected = jelly_candy.color
        jelly_candy.color = "blue"
        self.assertEqual(expected, jelly_candy.color)

    def test_color_property_positive(self):
        jelly_candy = JellyCandy()
        expected = jelly_candy.color
        jelly_candy.color = "red"
        self.assertEqual(expected, jelly_candy.color)

    def test_weight_property_with_zero(self):
        jelly_candy = JellyCandy()
        expected = jelly_candy.weight
        jelly_candy.weight = 0
        self.assertEqual(expected, jelly_candy.weight)

    def test_weight_property_negative(self):
        jelly_candy = JellyCandy()
        expected = jelly_candy.weight
        jelly_candy.weight = -10
        self.assertEqual(expected, jelly_candy.weight)

    def test_weight_property_positive(self):
        jelly_candy = JellyCandy()
        expected = 15
        jelly_candy.weight = 15
        self.assertEqual(expected, jelly_candy.weight)


if __name__ == "__main__":
    unittest.main()
