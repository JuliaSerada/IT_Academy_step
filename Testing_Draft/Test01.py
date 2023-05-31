def test_1_is_adult():
    human = Human(age=18)
    return human.is_adult()


def test_2_is_alive():
    human = Human(alive=True)
    return human.is_alive()


def test_3_get_alive_count():
    ls = [
        Human(alive=True),
        Human(alive=True),
        Human(alive=False)
    ]
    return HumanStatCalculator.get_alive_count(ls) == 2


def test_4_get_alive_count():
    ls = [Human(alive=True), Human(alive=True), Human(alive=False)]
    return HumanStatCalculator.get_not_alive_count(ls) == 1


def test_suite():
    msg = f"""
     test_1_is_adult = {test_1_is_adult()}
     test_2_is_alive = {test_2_is_alive()}
     test_3_get_alive_count = {test_3_get_alive_count()}
     test_4_get_alive_count = {test_4_get_alive_count()}
    """
    print(msg)
