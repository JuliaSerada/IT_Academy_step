from human import Human


class CountHuman:
    @staticmethod
    def count_adult(humans):
        count = 0

        if isinstance(humans, (list, tuple)):
            for human in humans:
                if isinstance(human, Human) and human.age >= 18:
                    count += 1

            return count

    @staticmethod
    def count_underage(humans):
        total = len(humans)
        total -= CountHuman.count_adult(humans)

        return total

    @staticmethod
    def is_alive_count(humans):
        alive_count = 0

        for human in humans:
            if human.is_alive == "Yes":
                alive_count += 1

        return alive_count

    @staticmethod
    def is_not_alive_count(humans):
        total = len(humans)
        total -= CountHuman.is_alive_count(humans)

        return total
