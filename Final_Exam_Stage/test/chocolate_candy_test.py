import unittest
from Final_Exam_Stage.entity.chocolate_candy import ChocolateCandy


class ChocolateCandyTest(unittest.TestCase):
    def test_chocolate_candy_default_constructor(self):
        chocolate_candy = ChocolateCandy()
        expected_ingredient = "nuts"
        expected_brand = "Snickers"
        expected_weight = 0
        expected_price = 0

        self.assertEqual(expected_ingredient, chocolate_candy.ingredient)
        self.assertEqual(expected_brand, chocolate_candy.brand)
        self.assertEqual(expected_weight, chocolate_candy.weight)
        self.assertEqual(expected_price, chocolate_candy.price)

    def test_chocolate_candy_constructor_with_args(self):
        expected_ingredient = "nuts"
        expected_brand = "Snickers"
        expected_weight = 95.5
        expected_price = 15

        chocolate_candy = ChocolateCandy(expected_ingredient, expected_brand, expected_weight, expected_price)

        self.assertEqual(expected_ingredient, chocolate_candy.ingredient)
        self.assertEqual(expected_brand, chocolate_candy.brand)
        self.assertEqual(expected_weight, chocolate_candy.weight)
        self.assertEqual(expected_price, chocolate_candy.price)

    def test_negative_chocolate_candy_with_invalid_ingredient(self):
        ingredient = "wafers"
        expected = "wafers"

        chocolate_candy = ChocolateCandy(ingredient=ingredient)

        self.assertEqual(expected, chocolate_candy.ingredient)

    def test_negative_chocolate_candy_brand(self):
        brand = "Snickers"
        expected = "Snickers"

        chocolate_candy = ChocolateCandy(brand=brand)

        self.assertEqual(expected, chocolate_candy.brand)

    def test_negative_chocolate_candy_weight(self):
        weight = -100
        expected = -100

        chocolate_candy = ChocolateCandy(weight=weight)

        self.assertEqual(expected, chocolate_candy.weight)

    def test_zero_chocolate_candy_weight(self):
        weight = 0
        expected = 0

        chocolate_candy = ChocolateCandy(weight=weight)

        self.assertEqual(expected, chocolate_candy.weight)

    def test_zero_chocolate_candy_price(self):
        price = 0
        expected = 0

        chocolate_candy = ChocolateCandy(price=price)

        self.assertEqual(expected, chocolate_candy.price)

    def test_ingredient_property_negative(self):
        chocolate_candy = ChocolateCandy()
        expected = chocolate_candy.ingredient
        chocolate_candy.ingredient = "wafers"
        self.assertEqual(expected, chocolate_candy.ingredient)

    def test_ingredient_property_positive(self):
        chocolate_candy = ChocolateCandy()
        expected = chocolate_candy.ingredient
        chocolate_candy.ingredient = "nuts"
        self.assertEqual(expected, chocolate_candy.ingredient)

    def test_weight_property_with_zero(self):
        chocolate_candy = ChocolateCandy()
        expected = chocolate_candy.weight
        chocolate_candy.weight = 0
        self.assertEqual(expected, chocolate_candy.weight)

    def test_weight_property_negative(self):
        chocolate_candy = ChocolateCandy()
        expected = chocolate_candy.weight
        chocolate_candy.weight = 0
        self.assertEqual(expected, chocolate_candy.weight)

    def test_weight_property_positive(self):
        chocolate_candy = ChocolateCandy()
        expected = 120
        chocolate_candy.weight = 120
        self.assertEqual(expected, chocolate_candy.weight)


if __name__ == "__main__":
    unittest.main()