from count_human import CountHuman
from create_human import HumanCreator


def main():
    ls = HumanCreator.create()
    adult = CountHuman.count_adult(ls)
    underage = CountHuman.count_underage(ls)

    for human in ls:
        msg = f"{human}"
        print(msg)

    print(f"Adult - {adult}")
    print(f"Underage - {underage}")
    print(f"Total alive - {CountHuman.is_alive_count(ls)}")
    print(f"Total not alive - {CountHuman.is_not_alive_count(ls)}")


if __name__ == '__main__':
    main()
