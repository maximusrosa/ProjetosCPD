from collections import namedtuple

Par = namedtuple('Par', ['lista', 'num_trocas'])

sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]


def main():
    with open("Sample Input.txt", "r") as file:

        num_datasets = int(file.readline())

        for i in range(num_datasets):
            file.read(1)  # pulando o '\n'

            inf_dataset = file.readline().rstrip('\n').split(' ')
            tam_strings = int(inf_dataset[0])
            num_strings = int(inf_dataset[1])

            lst_seq_dna = le_dataset(file, num_strings)          # cria uma lista de listas de chars (sequências de DNA)
            lst_pares = ordena_listas(lst_seq_dna, tam_strings)  # ordena essas listas com base no número de trocas

            for par in lst_pares:
                print(lst2str(par.lista))

            print('\n', end='')


# Função para converter uma lista de chars em uma string
def lst2str(lst):
    # initialization of string to ""
    str1 = ""

    # using join function join the list s by
    # separating words by str1
    return str1.join(lst)


# Função para armazenar as informações do dataset em uma lista de listas de chars
def le_dataset(file, num_strings):
    lst_seq_dna = []

    for i in range(num_strings):
        lst_seq_dna.append(split((file.readline().rstrip('\n'))))

    return lst_seq_dna


# Função para separar uma string em uma lista de chars
def split(word):
    return list(word)


def shell_sort(lista_x, list_size, gerador_h="ciura"):
    trocas_realizadas = 0

    # Sequência de Shell
    if gerador_h.lower() == "SHELL".lower():

        sublist_count = 1
        while sublist_count < (list_size // 2):
            sublist_count *= 2

        while sublist_count > 0:

            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

            sublist_count = sublist_count // 2

        # print(f"Total de trocas: {trocas_realizadas}")

    # Sequência de Knuth
    elif gerador_h.lower() == "KNUTH".lower():

        sublist_count = 1
        while sublist_count < (list_size // 3):
            sublist_count = 3 * sublist_count + 1

        while sublist_count > 0:
            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

            sublist_count = (sublist_count - 1) // 3

        # print(f"Total de trocas: {trocas_realizadas}")

    # Sequência de Ciura (para n < 701)
    elif gerador_h.lower() == "CIURA".lower():

        seq_ciura = filtro_ciura(list_size)

        for sublist_count in seq_ciura:
            for start_position in range(sublist_count):
                trocas_realizadas += gap_insertion_sort(lista_x, start_position, sublist_count, list_size)

        # print(f"Total de trocas: {trocas_realizadas}")

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


# Função para ordenar as listas conforme o número de trocas
def ordena_listas(lst_seq_dna, tam_lista):
    lst_pares = []

    for seq_dna in lst_seq_dna:
        par = Par._make([seq_dna.copy(),
                         shell_sort(seq_dna, tam_lista)])
        lst_pares.append(par)

    sort_tuple_list(lst_pares)

    return lst_pares


# Função para filtrar apenas números menores que o tamanho da lista
def filtro_ciura(list_size):
    return [num for num in sequencia_ciura if num < list_size]


# Function to sort the list by second item of tuple
def sort_tuple_list(tup_lst):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup_lst.sort(key=lambda x: x[1])

    return tup_lst


if __name__ == '__main__':
    main()

# Material usado como referência:
# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html
# https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/
# https://www.geeksforgeeks.org/python-convert-list-characters-string/
