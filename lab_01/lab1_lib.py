# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html

def main():
    lista_x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(lista_x)
    print(lista_x)


def shell_sort(lista_x):
    sublistcount = len(lista_x) // 2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gap_insertion_sort(lista_x, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", lista_x)

        sublistcount = sublistcount // 2


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
