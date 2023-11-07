# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html

import sys
from math import floor
import time


def main():

    print("Obtendo resultados...")
    if (sys.argv[1] == "entrada1.txt"):
        clear_file_if_exists("saida1.txt")
    else:
        clear_file_if_exists("saida2.txt")

    with open(sys.argv[1], "r") as file:
        # readlines() retorna uma lista de strings no qual cada string é uma linha do arquivo
        linhas_str = file.readlines()

        for linha in linhas_str:
            # split() retorna uma lista com cada "número" (na forma de texto) da linha
            lista_numeros = linha.split()
            # usando map() para conversão
            lista_numeros = list(map(int, lista_numeros))
            tamanho_lista = lista_numeros.pop(0)

            shell_sort(lista_numeros, tamanho_lista)

    print("Arquivo", "saida1.txt " if sys.argv[1] ==
          "entrada1.txt" else "saida2.txt", "criado com sucesso!")


def shell_sort(lista_x, list_size):

    if (sys.argv[1] == "entrada1.txt"):
        file_s1 = open("saida1.txt", "a")
    else:
        file_s2 = open("saida2.txt", "a")

    lst_cpy1 = lista_x.copy()
    lst_cpy2 = lista_x.copy()

    # Sequência de Shell
    if (sys.argv[1] == "entrada1.txt"):
        file_s1.write(f"{' '.join(str(s) for s in lista_x)} SEQ=SHELL\n")

    start_time = time.perf_counter()

    sublist_count = list_size // 2

    while sublist_count > 0:

        for start_position in range(sublist_count):
            gap_insertion_sort(lista_x, start_position,
                               sublist_count, list_size)
        if (sys.argv[1] == "entrada1.txt"):
            file_s1.write(
                f"{' '.join(str(s) for s in lista_x)} INCR={sublist_count}\n")

        sublist_count = sublist_count // 2

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if (sys.argv[1] == "entrada2.txt"):
        file_s2.write(
            f"SHELL, {list_size}, {elapsed_time * 1000:.6f}, 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz 2.42 GHz\n")

    lista_x = lst_cpy1

    # Sequência de Knuth
    if (sys.argv[1] == "entrada1.txt"):
        file_s1.write(f"{' '.join(str(s) for s in lista_x)} SEQ=KNUTH\n")

    start_time = time.perf_counter()

    sublist_count = 1
    while sublist_count <= (list_size // 3):
        sublist_count = 3 * sublist_count + 1

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(lista_x, start_position,
                               sublist_count, list_size)
        if (sys.argv[1] == "entrada1.txt"):
            file_s1.write(
                f"{' '.join(str(s) for s in lista_x)} INCR={sublist_count}\n")

        sublist_count = (sublist_count - 1) // 3

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if (sys.argv[1] == "entrada2.txt"):
        file_s2.write(
            f"KNUTH, {list_size}, {elapsed_time * 1000:.6f}, 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz 2.42 GHz\n")

    lista_x = lst_cpy2

    # Sequência de Ciura
    if (sys.argv[1] == "entrada1.txt"):
        file_s1.write(f"{' '.join(str(s) for s in lista_x)} SEQ=CIURA\n")

    start_time = time.perf_counter()

    sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]

    if (list_size <= 701):
        for i in range(len(sequencia_ciura)):
            if sequencia_ciura[i] >= list_size >= sequencia_ciura[i + 1]:
                # corta a lista na posição i + 1
                sequencia_ciura = sequencia_ciura[i + 1:]
                break

    else:
        h_ciura = 701
        while (list_size > h_ciura):
            h_ciura = floor(h_ciura * 2.25)  # arredonda pra baixo
            sequencia_ciura.insert(0, h_ciura)

    for sublist_count in sequencia_ciura:
        for start_position in range(sublist_count):
            gap_insertion_sort(lista_x, start_position,
                               sublist_count, list_size)
        if (sys.argv[1] == "entrada1.txt"):
            file_s1.write(
                f"{' '.join(str(s) for s in lista_x)} INCR={sublist_count}\n")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if (sys.argv[1] == "entrada2.txt"):
        file_s2.write(
            f"CIURA, {list_size}, {elapsed_time * 1000:.6f}, 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz 2.42 GHz\n")


def gap_insertion_sort(lista_x, start, gap, list_size):

    for i in range(start + gap, list_size, gap):

        current_value = lista_x[i]
        position = i

        while position >= gap and lista_x[position - gap] > current_value:
            lista_x[position] = lista_x[position - gap]
            position = position - gap

        lista_x[position] = current_value


def clear_file_if_exists(filename):
    with open(filename, "w") as file:
        pass


if __name__ == '__main__':
    main()
