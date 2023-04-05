# The program that checks is the randomly generated list (vector) with the different values

import model_logic
import value


def main():
    size = int(input("Input size of list: "))
    ls = value.create_list(size)
    value.rand_init(ls)
    msg = value.convert(ls)
    print("The list:", msg)
    model_logic.is_different(ls)
    print(f"This list is different: {model_logic.is_different(ls)}.")


if __name__ == "__main__":
    main()
