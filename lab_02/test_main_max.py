import random, statistics

def quicksort(lista_x, first, last, pivot_choice='rand'):
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
        pivot_position = random.randint(first, last)
        lista_x[first], lista_x[pivot_position] = lista_x[pivot_position], lista_x[first]
        #swaps += 1

    elif pivot_choice.lower() == 'md3'.lower():
        pivot_value = statistics.median([lista_x[first], lista_x[last], lista_x[(first + last) // 2]])

        for num in lista_x:
            if num == pivot_value:
                pivot_position = lista_x.index(num)
                break

        lista_x[first], lista_x[pivot_position] = lista_x[pivot_position], lista_x[first]
        #swaps += 1

    else:
        assert False, "Escolha de particionador inválida."

    pivot_value = lista_x[first]
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




def test_quicksort():
    # exemplo site usp
    assert quicksort([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 9 - 1) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

    # exemplos do sor
    assert quicksort([16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert quicksort([3, 10, 5, 16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # exemplos extremos
    assert quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert quicksort([16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 16 - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # exemplo vídeo professor Isidro
    assert quicksort([25, 57, 48, 37, 12, 92, 33], 0, 7 - 1) == [12, 25, 33, 37, 48, 57, 92]

    # só pra garantir
    assert quicksort([20, 2, 9, 7, 12, 15, 1, 6, 8], 0, 9 - 1) == [1, 2, 6, 7, 8, 9, 12, 15, 20]



    