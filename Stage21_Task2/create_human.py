import random
from human import Human


class HumanCreator:
    @staticmethod
    def create(size=8):
        humans = []
        FIRST_NAMES = ("Mary", "Nikita", "Liza", "Philip", "David", "Julia", "Emily", "Harry")
        SURNAMES = ("Smith", "Brown", "Jonson", "Rogers", "Young", "Lee", "Green", "Potter")
        MAX_AGE = 100
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.first_name = random.choice(FIRST_NAMES)
            human.surname = random.choice(SURNAMES)
            human.age = random.randint(MIN_AGE, MAX_AGE)
            human.is_alive = random.choice((True, False))
            humans.append(human)

        return humans
