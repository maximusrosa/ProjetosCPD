"""
Implementação do algoritmo quicksort utilizando o particionamento de Hoare com duas escolhas de particionador:
Mediana de 3 e Escolha Aleatória

Informações da saída: tamanho da entrada, número de trocas, número de chamadas recursivas, tempo de execução
"""

from time import perf_counter
from random import randint
global swaps, rec_count

def quicksort(lista_x, first, last, pivot_choice):
    global rec_count

    if first >= last:
        return
    else:
        splitpoint = partition(lista_x, first, last, pivot_choice)

        quicksort(lista_x, first, splitpoint - 1, pivot_choice)
        rec_count += 1
        quicksort(lista_x, splitpoint + 1, last, pivot_choice)
        rec_count += 1

    return lista_x

def partition(lista_x, first, last, pivot_choice):
    global swaps

    if pivot_choice.lower() == 'rand'.lower():
        pivot_index = randint(first, last)
        lista_x[first], lista_x[pivot_index] = lista_x[pivot_index], lista_x[first]
        pivot_value = lista_x[first]
        swaps += 1

    elif pivot_choice.lower() == 'md3'.lower():
        pivot_value, pivot_index = mediana_de_3(lista_x, first, last)

        lista_x[first], lista_x[pivot_index] = lista_x[pivot_index], lista_x[first]
        swaps += 1

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
            swaps += 1

    # coloca o pivô na posição correta
    lista_x[first], lista_x[rightmark] = lista_x[rightmark], lista_x[first]
    swaps += 1

    return rightmark

def mediana_de_3(lista, first, last):
    middle = (first + last) // 2

    # Create a list of tuples where each tuple is (value, index)
    candidates = [(lista[first], first), (lista[middle], middle), (lista[last], last)]

    # Sort the list of tuples by the first element of each tuple (the value)
    candidates.sort(key=lambda x: x[0])

    # Return the second element of the second tuple (the median value and its index)
    return candidates[1]


def main():
    global swaps, rec_count

    with open("entrada-quicksort.txt", "r") as input_file:
        linhas_arq = input_file.readlines()

        for linha in linhas_arq:
            lista_num = list(map(int, linha.split()))
            tam_lista = lista_num.pop(0)

            print(f"TAMANHO ENTRADA {tam_lista}")

            swaps = rec_count = 0

            start_time = perf_counter()
            quicksort(lista_num, 0, tam_lista - 1, 'md3')
            end_time = perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # em milissegundos

            print(f"SWAPS {swaps}")
            print(f"RECURSOES {rec_count}")
            print(f"TEMPO {elapsed_time:.3f}")
            print('\n', end='')

    print("Deu bom carai")


if __name__ == "__main__":
    main()

# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
