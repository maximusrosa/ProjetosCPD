# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html

sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]


def main():

    lista_tst1 = [16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5]
    shell_sort(lista_tst1, len(lista_tst1), "SHELL")

    lista_tst1 = [16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5]
    shell_sort(lista_tst1, len(lista_tst1), "KNUTH")

    print("\n-------------------------------------------------\n")

    lista_tst2 = [3, 10, 5, 16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7]
    shell_sort(lista_tst2, len(lista_tst2), "SHELL")

    lista_tst2 = [3, 10, 5, 16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7]
    shell_sort(lista_tst2, len(lista_tst2), "KNUTH")


def shell_sort(lista_x, tamanho_lista, gerador_h="SHELL"):

    # Sequência de Shell
    if gerador_h.lower() == "SHELL".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=SHELL")

        sublist_count = tamanho_lista // 2

        while sublist_count > 0:

            for start_position in range(sublist_count):
                gap_insertion_sort(lista_x, start_position, sublist_count)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")

            sublist_count = sublist_count // 2

    # Sequência de Knuth
    elif gerador_h.lower() == "KNUTH".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=KNUTH")

        sublist_count = 1
        while sublist_count <= (tamanho_lista // 3):
            sublist_count = 3 * sublist_count + 1

        while sublist_count > 0:
            for start_position in range(sublist_count):
                gap_insertion_sort(lista_x, start_position, sublist_count)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")

            sublist_count = (sublist_count - 1) // 3

    # Sequência de Ciura (tem que testar ainda)
    elif gerador_h.lower() == "CIURA".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=CIURA")

        for sublist_count in sequencia_ciura:
            for start_position in range(sublist_count):
                gap_insertion_sort(lista_x, start_position, sublist_count)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")


def gap_insertion_sort(lista_x, start, gap):
    for i in range(start + gap, len(lista_x), gap):

        current_value = lista_x[i]
        position = i

        while position >= gap and lista_x[position - gap] > current_value:
            lista_x[position] = lista_x[position - gap]
            position = position - gap

        lista_x[position] = current_value


if __name__ == '__main__':
    main()
