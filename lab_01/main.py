import sys
import lab1_lib


def main():
    with open("entrada1.txt", "r") as file:
        # readlines() retorna uma lista de strings no qual cada string é uma linha do arquivo
        linhas_str = file.readlines()

        for linha in linhas_str:
            # split() retorna uma lista com cada "número" (na forma de texto) da linha
            lista_numeros = linha.split()
            # usando map() para conversão
            lista_numeros = list(map(int, lista_numeros))
            tamanho_lista = lista_numeros.pop(0)

            lab1_lib.shell_sort(lista_numeros, tamanho_lista)
            break


main()