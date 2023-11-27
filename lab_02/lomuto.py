import random
global swaps, rec_count

def quicksort(lista_x, low, high, pivot_choice):
    global rec_count

    if low < high:
        pivot = partition(lista_x, low, high, pivot_choice)
        quicksort(lista_x, low, pivot - 1, pivot_choice)
        rec_count += 1
        quicksort(lista_x, pivot + 1, high, pivot_choice)
        rec_count += 1

    return lista_x

def partition(lista_x, low, high, pivot_choice):
    global swaps

    if pivot_choice == "aleatorio":
        # Random partition
        random_index = random.randint(low, high)
        lista_x[random_index], lista_x[high] = lista_x[high], lista_x[random_index]
        swaps += 1

    elif pivot_choice == "mediana":
        # Median partition
        middle_index = (low + high) // 2
        if lista_x[low] > lista_x[middle_index]:
            lista_x[low], lista_x[middle_index] = lista_x[middle_index], lista_x[low]
            swaps += 1
        if lista_x[low] > lista_x[high]:
            lista_x[low], lista_x[high] = lista_x[high], lista_x[low]
            swaps += 1
        if lista_x[middle_index] > lista_x[high]:
            lista_x[middle_index], lista_x[high] = lista_x[high], lista_x[middle_index]
            swaps += 1

    pivot = lista_x[high]
    i = low - 1

    for j in range(low, high):
        if lista_x[j] <= pivot:
            i += 1
            lista_x[i], lista_x[j] = lista_x[j], lista_x[i]
            swaps += 1

    lista_x[i + 1], lista_x[high] = lista_x[high], lista_x[i + 1]
    swaps += 1
    return i + 1


print(quicksort([3, 2, 1, 5, 4], 0, 4, "mediana"))