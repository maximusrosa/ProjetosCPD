import sys
import lab1_lib


def main():
    with open("numeros.csv", "r") as file:
        lista_x = [int(x) for x in file.read().split(",")]


main()
