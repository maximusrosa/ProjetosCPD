"""
Arquivo de Testes
"""

from random import randint


def quicksort(lista_x, first, last, pivot_choice='md3'):
    #global rec_count

    if first >= last:
        return
    else:
        splitpoint = partition(lista_x, first, last, pivot_choice)

        quicksort(lista_x, first, splitpoint - 1, pivot_choice)
        #rec_count += 1
        quicksort(lista_x, splitpoint + 1, last, pivot_choice)
        #rec_count += 1

    return lista_x

def partition(lista_x, first, last, pivot_choice):
    #global swaps

    if pivot_choice.lower() == 'rand'.lower():
        pivot_index = randint(first, last)
        lista_x[first], lista_x[pivot_index] = lista_x[pivot_index], lista_x[first]
        pivot_value = lista_x[first]
        #swaps += 1

    elif pivot_choice.lower() == 'md3'.lower():
        pivot_value, pivot_index = mediana_de_3(lista_x, first, last)

        lista_x[first], lista_x[pivot_index] = lista_x[pivot_index], lista_x[first]
        #swaps += 1

    else:
        assert False, "Escolha de particionador inválida."

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and lista_x[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while lista_x[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            lista_x[leftmark], lista_x[rightmark] = lista_x[rightmark], lista_x[leftmark]
            #swaps += 1

    # coloca o pivô na posição correta
    lista_x[first], lista_x[rightmark] = lista_x[rightmark], lista_x[first]
    #swaps += 1

    return rightmark

def mediana_de_3(lista, first, last):
    middle = (first + last) // 2

    # Create a list of tuples where each tuple is (value, index)
    candidates = [(lista[first], first), (lista[middle], middle), (lista[last], last)]

    # Sort the list of tuples by the first element of each tuple (the value)
    candidates.sort(key=lambda x: x[0])

    # Return the second element of the second tuple (the median value and its index)
    return candidates[1]


def test_mediana_de_3():
    assert mediana_de_3([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 9 - 1) == (54, 0)
    assert mediana_de_3([25, 57, 48, 37, 12, 92, 33], 0, 7 - 1) == (33, 6)
    assert mediana_de_3([20, 2, 9, 7, 12], 0, 5 - 1) == (12, 4)

    assert mediana_de_3([1, 2, 3], 0, 3 - 1) == (2, 1)
    assert mediana_de_3([3, 2, 1], 0, 3 - 1) == (2, 1)
    assert mediana_de_3([1, 3, 2], 0, 3 - 1) == (2, 2)
    assert mediana_de_3([1, 2, 3, 4], 0, 4 - 1) == (2, 1)
    assert mediana_de_3([4, 3, 2, 1], 0, 4 - 1) == (3, 1)
    assert mediana_de_3([2, 3, 1, 4], 0, 4 - 1) == (3, 1)
    assert mediana_de_3([1, 2, 3, 4, 5], 0, 5 - 1) == (3, 2)
    assert mediana_de_3([3, 4, 5, 2, 1], 0, 5 - 1) == (3, 0)
    assert mediana_de_3([1, 3, 2, 5, 4], 0, 5 - 1) == (2, 2)
    assert mediana_de_3([10, 50, 30], 0, 3 - 1) == (30, 2)
    assert mediana_de_3([30, 50, 10], 0, 3 - 1) == (30, 0)
    assert mediana_de_3([10, 30, 50], 0, 3 - 1) == (30, 1)


def test_quicksort():
    # exemplo vídeo professor Isidro
    assert quicksort([25, 57, 48, 37, 12, 92, 33], 0, 7 - 1) == [12, 25, 33, 37, 48, 57, 92]

    # exemplo site usp
    assert quicksort([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 9 - 1) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

    # exemplos do sor
    assert quicksort([16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert quicksort([3, 10, 5, 16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # exemplos extremos
    assert quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert quicksort([16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # só pra garantir
    assert quicksort([20, 2, 9, 7, 12, 15, 1, 6, 8], 0, 9 - 1) == [1, 2, 6, 7, 8, 9, 12, 15, 20]

    # additional tests with repeated values
    assert quicksort([2, 2, 4, 4, 6, 6, 8, 8], 0, 8 - 1) == [2, 2, 4, 4, 6, 6, 8, 8]
    assert quicksort([9, 9, 7, 7, 5, 5, 3, 3], 0, 8 - 1) == [3, 3, 5, 5, 7, 7, 9, 9]
    assert quicksort([1, 1, 3, 3, 5, 5, 7, 7], 0, 8 - 1) == [1, 1, 3, 3, 5, 5, 7, 7]
    assert quicksort([6, 6, 4, 4, 2, 2, 8, 8], 0, 8 - 1) == [2, 2, 4, 4, 6, 6, 8, 8]
    assert quicksort([7, 7, 5, 5, 3, 3, 9, 9], 0, 8 - 1) == [3, 3, 5, 5, 7, 7, 9, 9]
    assert quicksort([1, 1, 1, 1, 1, 1, 1, 1], 0, 8 - 1) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert quicksort([2, 2, 2, 2, 1, 1, 1, 1], 0, 8 - 1) == [1, 1, 1, 1, 2, 2, 2, 2]
    assert quicksort([3, 3, 3, 2, 2, 2, 1, 1], 0, 8 - 1) == [1, 1, 2, 2, 2, 3, 3, 3]
















    