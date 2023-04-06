# The program checks if all elements of the randomly generated list(vector) are sorted in ascending order
import business_logic
import size_ls


def main():
    size = int(input("Input the size of list: "))
    ls = size_ls.create_list(size)
    size_ls.rand_init(ls)
    msg = size_ls.convert(ls)
    print("The list:", msg)
    business_logic.is_sorted_asc(ls)
    print(f"This list is sorted in ascending order: {business_logic.is_sorted_asc(ls)}.")


if __name__ == "__main__":
    main()
