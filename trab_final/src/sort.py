from src.hash_table import Jogador


def quicksort(lst: list[Jogador]) -> list[Jogador]:
    """
    This function performs quicksort using the hoare partition scheme and the median-of-3 pivot choice on a list of Jogador objects.
    If the list is smaller than 15 elements, it uses the insertion sort for efficiency. Otherwise, it uses the quicksort algorithm.
    """
    if len(lst) < 15:
        return insertion_sort(lst)
    else:
        return _quicksort(lst, 0, len(lst) - 1)


def insertion_sort(lst: list[Jogador]) -> list[Jogador]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key.media_global > lst[j].media_global:  # change to '<' for ascending order
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst


def _quicksort(lst, first, last):
    if first >= last:
        return

    else:
        splitpoint = partition(lst, first, last)
        _quicksort(lst, first, splitpoint - 1)
        _quicksort(lst, splitpoint + 1, last)

    return lst


def partition(lst, first, last):
    pivot_value, pivot_index = median_of_3(lst, first, last)
    lst[first], lst[pivot_index] = lst[pivot_index], lst[first]

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and lst[leftmark].media_global >= pivot_value:
            leftmark = leftmark + 1
        while lst[rightmark].media_global < pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            lst[leftmark], lst[rightmark] = lst[rightmark], lst[leftmark]

    lst[first], lst[rightmark] = lst[rightmark], lst[first]

    return rightmark


def median_of_3(lst, first, last):
    middle = (first + last) // 2

    candidates = [(lst[first].media_global, first), (lst[middle].media_global, middle), (lst[last].media_global, last)]
    candidates.sort(key=lambda x: x[0], reverse=True)

    return candidates[1]



def merge_sort(lst: list[tuple[Jogador, float]]) -> list[tuple[Jogador, float]]:
    """
    This function performs merge sort using the top-down approach on a list of tuples (Jogador, float).
        The list is sorted in descending order first by the float value and then by the media_global attribute of the Jogador object:
        1. If the float values are equal, the Jogador objects are sorted by their media_global attribute in descending order.
        2. If the float values are different, the Jogador objects are sorted by the float value in descending order.
        The function returns the sorted list of tuples.
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] == right[j][1]:
            if left[i][0].media_global >= right[j][0].media_global:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result
