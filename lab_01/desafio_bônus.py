# Material usado como referência:
# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html
# https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/

from collections import namedtuple

Par = namedtuple('Par', ['lista', 'num_trocas'])

sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]


def main():
    lista_tst1 = [16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5]
    lista_tst2 = [3, 10, 5, 16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7]

    # Cria uma tupla com a lista original e o número de trocas realizadas para ordená-la
    par_L1 = Par._make([lista_tst1.copy(),
                        shell_sort(lista_tst1, len(lista_tst1), "CIURA")])

    print("\n-------------------------------------------------\n")

    par_L2 = Par._make([lista_tst2.copy(),
                        shell_sort(lista_tst2, len(lista_tst2), "CIURA")])

    lst_pares = [par_L1, par_L2]

    sort_tuple_list(lst_pares)

    print("\n-------------------------------------------------\n")

    for par in lst_pares:
        print(f"Lista: {par.lista}", f"Total de trocas: {par.num_trocas}")


def shell_sort(lista_x, list_size, gerador_h="SHELL"):
    trocas_realizadas = 0

    # Sequência de Shell
    if gerador_h.lower() == "SHELL".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=SHELL")

        sublist_count = list_size // 2

        while sublist_count > 0:

            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")

            sublist_count = sublist_count // 2

        #print(f"Total de trocas: {trocas_realizadas}")

    # Sequência de Knuth
    elif gerador_h.lower() == "KNUTH".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=KNUTH")

        sublist_count = 1
        while sublist_count <= (list_size // 3):
            sublist_count = 3 * sublist_count + 1

        while sublist_count > 0:
            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")

            sublist_count = (sublist_count - 1) // 3

        #print(f"Total de trocas: {trocas_realizadas}")

    # Sequência de Ciura (para n ≤ 701)
    elif gerador_h.lower() == "CIURA".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ=CIURA")

        seq_ciura = filtro_ciura(list_size)

        for sublist_count in seq_ciura:
            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

            print(' '.join(str(s) for s in lista_x), f"INCR={sublist_count}")

        #print(f"Total de trocas: {trocas_realizadas}")

    return trocas_realizadas


def gap_insertion_sort(lista_x, start, gap, list_size):
    trocas = 0

    for i in range(start + gap, list_size, gap):
        current_value = lista_x[i]
        position = i

        while position >= gap and lista_x[position - gap] > current_value:
            lista_x[position] = lista_x[position - gap]
            position = position - gap
            trocas += 1

        lista_x[position] = current_value

    return trocas


# Função para filtrar a sequência de Ciura para n ≤ 701
def filtro_ciura(list_size):
    return [num for num in sequencia_ciura if num <= list_size]


# Function to sort the list by second item of tuple
def sort_tuple_list(tup_lst):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup_lst.sort(key=lambda x: x[1])

    return tup_lst


if __name__ == '__main__':
    main()
