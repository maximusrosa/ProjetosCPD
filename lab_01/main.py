import sys
import lab1_lib


def main():
    with open(sys.argv[1] + ".csv", "r") as file:
        list_x = [int(x) for x in file.read().split(",")]
        lab1_lib.shell_sort(list_x)
        print(list_x)


main()
