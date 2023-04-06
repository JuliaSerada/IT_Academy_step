from laptop import Laptop
from manager import Manager


def main():
    ls = [Laptop(brand="Apple", model="Macbook Air Pro 14", price=1600, number=55),
          Laptop(brand="Acer", model="Acer Chromebook Spin 714", price=679, number=22),
          Laptop(brand="HP", model="HP ENVY x360", price=1300, number=20),
          Laptop(brand="Lenovo", model="Lenovo Yoga 9i 14", price=1234, number=15)]

    msg = f"Total amount of laptops: {Manager.total_amount(ls)} $."
    print(msg)

    print(f"Max price: {Manager.get_max_price(ls)}")
    print(f"Min price: {Manager.get_min_price(ls)}")


if __name__ == "__main__":
    main()
