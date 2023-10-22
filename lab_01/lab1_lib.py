# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html

sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]


def main():
    list_x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(list_x)
    print(list_x)


def shell_sort(list_x, gerador_h="SHELL"):

    # Sequência de Shell
    if gerador_h.lower() == "SHELL".lower():
        sublistcount = len(list_x) // 2

        while sublistcount > 0:

            for startposition in range(sublistcount):
                gap_insertion_sort(list_x, startposition, sublistcount)

            print("After increments of size", sublistcount,
                  "the list is", list_x)

            sublistcount = sublistcount // 2

    # Sequência de Ciura
    # elif gerador_h.lower == "CIURA".lower():

    # Sequência de Knuth
    # elif gerador_h.lower == "KNUTH".lower():


def gap_insertion_sort(list_x, start, gap):
    for i in range(start + gap, len(list_x), gap):

        currentvalue = list_x[i]
        position = i

        while position >= gap and list_x[position - gap] > currentvalue:
            list_x[position] = list_x[position - gap]
            position = position - gap

        list_x[position] = currentvalue


if __name__ == '__main__':
    main()
