class Manager:

    @staticmethod
    def total_amount(ls):
        total_amount = 0

        for unit in ls:
            total_amount += unit.get_price()

        return total_amount

    @staticmethod
    def get_max_price(ls):
        max_laptop = ls[0]

        for unit in ls:
            if unit.get_price() > max_laptop.get_price():
                max_laptop = unit

        return max_laptop

    @staticmethod
    def get_min_price(ls):
        min_laptop = ls[0]

        for unit in ls:
            if unit.get_price() < min_laptop.get_price():
                min_laptop = unit

        return min_laptop
