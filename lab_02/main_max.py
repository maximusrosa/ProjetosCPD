# Objetivo: Implementar o quicksort utilizando o particionamento de Hoare com duas escolhas de particionador:
# Mediana de 3 e Escolha Aleatória

def main():
    lista_x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    tam_lista_x = len(lista_x)

    print(quicksort(lista_x, tam_lista_x))


# quicksort: ListaDeNúmeros Número -> ListaDeNúmeros
def quicksort(lista_x, tam_lista_x):
    quicksort_helper(lista_x, 0, tam_lista_x - 1)

    return lista_x


def quicksort_helper(lista_x, first, last):
    if first < last:
        splitpoint = partition(lista_x, first, last)

        quicksort_helper(lista_x, first, splitpoint - 1)
        quicksort_helper(lista_x, splitpoint + 1, last)


def partition(lista_x, first, last):
    pivotvalue = lista_x[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and lista_x[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while lista_x[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = lista_x[leftmark]
            lista_x[leftmark] = lista_x[rightmark]
            lista_x[rightmark] = temp

    temp = lista_x[first]
    lista_x[first] = lista_x[rightmark]
    lista_x[rightmark] = temp

    return rightmark


if __name__ == "__main__":
    main()

# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
