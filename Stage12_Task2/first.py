# The program that checks is the mirror list
import project_logic


def main():
    ls = [1, 2, 3, 4, 4, 3, 2, 1]
    print(f"This is the mirror list: {project_logic.is_mirror(ls)}.")


if __name__ == "__main__":
    main()
