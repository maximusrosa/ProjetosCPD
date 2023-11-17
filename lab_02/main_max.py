from time import perf_counter
from random import randint
from statistics import median

# Implementação do algoritmo quicksort utilizando o particionamento de Hoare com duas escolhas de particionador:
# Mediana de 3 e Escolha Aleatória

# Informações da saída: tamanho da entrada, número de trocas, número de chamadas recursivas, tempo de execução

def main():
    global swaps, rec_count

    print("Iniciando execução do algoritmo quicksort com particionamento de Hoare e mediana de 3.")
    #output_file = open("stats-mediana-hoare.txt", "a")

    with open("entrada-quicksort.txt", "r") as input_file:
        linhas_str = input_file.readlines()

        for linha in linhas_str:
            lista_num = linha.split()
            lista_num = list(map(int, lista_num))
            tam_lista = lista_num.pop(0)

            #output_file.write(f"TAMANHO ENTRADA {tam_lista}\n")
            print(f"TAMANHO ENTRADA {tam_lista}")

            swaps = rec_count = 0

            start_time = perf_counter()
            quicksort_hoare(lista_num, 0, tam_lista - 1, 'md3')
            end_time = perf_counter()
            elapsed_time = (end_time - start_time) * 1000

            #output_file.write(f"SWAPS {swaps}\n"
            #                  f"RECURSOES {rec_count}\n"
            #                  f"TEMPO {elapsed_time:.3f}\n")
            print(f"SWAPS {swaps}")
            print(f"RECURSOES {rec_count}")
            print(f"TEMPO {elapsed_time:.3f}")

    #output_file.close()
    print("Fim da execução.")


def quicksort_hoare(lista_x, first, last, pivot_choice='rand'):
    global rec_count

    if first >= last:
        return
    else:
        splitpoint = partition(lista_x, first, last, pivot_choice)

        quicksort_hoare(lista_x, first, splitpoint - 1, pivot_choice)
        rec_count += 1
        quicksort_hoare(lista_x, splitpoint + 1, last, pivot_choice)
        rec_count += 1

    return lista_x

def partition(lista_x, first, last, pivot_choice):
    global swaps

    if pivot_choice.lower() == 'rand'.lower():
        pivot_position = randint(first, last)
        lista_x[first], lista_x[pivot_position] = lista_x[pivot_position], lista_x[first]
        swaps += 1

    elif pivot_choice.lower() == 'md3'.lower():
        pivot_value = median([lista_x[first], lista_x[last], lista_x[(first + last) // 2]])

        for num in lista_x:
            if num == pivot_value:
                pivot_position = lista_x.index(num)
                break

        lista_x[first], lista_x[pivot_position] = lista_x[pivot_position], lista_x[first]
        swaps += 1

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
            swaps += 1

    # coloca o pivô na posição correta        
    lista_x[first], lista_x[rightmark] = lista_x[rightmark], lista_x[first]
    swaps += 1

    return rightmark


if __name__ == "__main__":
    main()

# Material usado como referência: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
