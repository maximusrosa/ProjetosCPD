import sys
import lab1_lib


def main():
    with open("numeros.csv", "r") as file:
        # leia os números separados por vírgula do arquivo e coloque-os em uma lista
        list_x = [int(x) for x in file.read().split(";")]

        lab1_lib.shell_sort(list_x, sys.argv[1])
        print(list_x)


main()
