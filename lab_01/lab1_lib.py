# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html

sequencia_ciura = [701, 301, 132, 57, 23, 10, 4, 1]


def main():
    lista_x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(lista_x, len(lista_x))


def shell_sort(lista_x, tamanho_lista, gerador_h="SHELL"):

    # Sequência de Shell
    if gerador_h.lower() == "SHELL".lower():
        print(' '.join(str(s) for s in lista_x), "SEQ==SHELL")

        sublistcount = tamanho_lista // 2

        while sublistcount > 0:

            for startposition in range(sublistcount):
                gap_insertion_sort(lista_x, startposition, sublistcount)

            print(' '.join(str(s) for s in lista_x), "INCR==", sublistcount)

            sublistcount = sublistcount // 2

    # Sequência de Ciura
    # elif gerador_h.lower == "CIURA".lower():

    # Sequência de Knuth
    # elif gerador_h.lower == "KNUTH".lower():


def gap_insertion_sort(lista_x, start, gap):
    for i in range(start + gap, len(lista_x), gap):

        currentvalue = lista_x[i]
        position = i

        while position >= gap and lista_x[position - gap] > currentvalue:
            lista_x[position] = lista_x[position - gap]
            position = position - gap

        lista_x[position] = currentvalue


if __name__ == '__main__':
    main()
