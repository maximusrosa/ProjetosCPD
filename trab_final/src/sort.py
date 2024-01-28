from random import randint
import numpy as np


def random_lst(tam):
    generator = np.random.RandomState()
    lst = list(generator.randint(1, 1000, tam))

    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst


def quicksort(lst, first, last):
    if first >= last:
        return
    else:
        # Continue with the quicksort algorithm
        splitpoint = partition(lst, first, last, "mediana")

        quicksort(lst, first, splitpoint - 1)
        quicksort(lst, splitpoint + 1, last)

    return lst


def partition(lst, first, last, pivot_choice):
    if pivot_choice == "aleatorio":
        pivot_index = randint(first, last)
        lst[first], lst[pivot_index] = lst[pivot_index], lst[first]
        pivot_value = lst[first]

    elif pivot_choice == "mediana":
        pivot_value, pivot_index = mediana_de_3(lst, first, last)

        lst[first], lst[pivot_index] = lst[pivot_index], lst[first]

    else:
        assert False, "Escolha de pivô inválida."

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and lst[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while lst[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            lst[leftmark], lst[rightmark] = lst[rightmark], lst[leftmark]

    # coloca o pivô na posição correta
    lst[first], lst[rightmark] = lst[rightmark], lst[first]

    return rightmark


def mediana_de_3(lst, first, last):
    middle = (first + last) // 2

    # Create a list of tuples where each tuple is (value, index)
    candidates = [(lst[first], first), (lst[middle], middle), (lst[last], last)]

    # Sort the list of tuples by the first element of each tuple (the value)
    candidates.sort(key=lambda x: x[0])

    # Return the second element of the second tuple (the median value and its index)
    return candidates[1]


def merge(lst, left, mid, right):
    left_copy = lst[left:mid + 1]
    right_copy = lst[mid + 1:right + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            lst[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            lst[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        lst[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        lst[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort_bu(lst):
    size = 1
    while size < len(lst):
        for i in range(0, len(lst), size * 2):
            mid = i + size - 1
            right = min(i + size * 2 - 1, len(lst) - 1)
            merge(lst, i, mid, right)
        size *= 2
    return lst


def sort(lst, method='quicksort'):
    if len(lst) < 15:
        insertion_sort(lst)

    elif method == 'quicksort':
        quicksort(lst, 0, len(lst) - 1)

    elif method == 'merge':
        merge_sort_bu(lst)

    else:
        assert False, "Método de ordenação inválido."
