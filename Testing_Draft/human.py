@staticmethod
    def is_alive_count(humans):
        ls = HumanCreator.create(humans)
        alive_count = 0
        for human in ls:
            if human.is_alive:
                alive_count += 1
            return alive_count

    @staticmethod
    def is_not_alive_count(humans):
        total = len(humans)
        total -= CountHuman.is_alive_count(humans)
        return total
