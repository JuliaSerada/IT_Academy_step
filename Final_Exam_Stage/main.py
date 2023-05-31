from Final_Exam_Stage.entity.chocolate_candy import ChocolateCandy
from Final_Exam_Stage.entity.lollipop import Lollipop
from Final_Exam_Stage.entity.jelly_candy import JellyCandy
from Final_Exam_Stage.container.new_year_gift import NewYearGift
from Final_Exam_Stage.logic.gift_assistance import GiftAssistance


def main():
    gift = NewYearGift()

    choc = ChocolateCandy("nuts", "Snickers", 115.5, 5)
    lol = Lollipop("apple", 15.0, 5)
    jel = JellyCandy("red", 4.2, 5.5)

    gift.add(choc)
    gift.add(lol)
    gift.add(jel)
    print(f"Total amount of sweets = {gift.size}")

    print(gift)

    total = GiftAssistance.calculate_total_weight(gift)
    print(f"Total weight of New Year Gift is {total} grams.")

    total = GiftAssistance.calculate_total_price(gift)
    print(f"Total price of New Year Gift is {total} $.")


if __name__ == "__main__":
    main()
