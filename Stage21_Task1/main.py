from zebra import Zebra
import random


def main():
    zebra1 = Zebra("Marty")
    zebra2 = Zebra("Alex")
    zebra3 = Zebra("Lily")

    zebras = (zebra1, zebra2, zebra3)

    for _ in range(10):
        zebra = random.choice(zebras)
        msg = f"Zebra with name - {zebra} is created: {zebra.get_stripe()}."
        print(msg)


if __name__ == "__main__":
    main()
