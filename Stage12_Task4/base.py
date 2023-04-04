# The program that counts the number of only even elements of a randomly generated list (vector)
import logic
import util


def main():
    size = int(input("Input size of list: "))
    ls = util.create_list(size)
    util.rand_init(ls)
    msg = util.convert(ls)
    print("The list:", msg)
    logic.count_even_element(ls)
    print(f"Total count of the even elements: {logic.count_even_element(ls)}.")


if __name__ == "__main__":
    main()
