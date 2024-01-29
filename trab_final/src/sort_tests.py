from sort import insertion_sort, merge_sort_bu, quicksort, mediana_de_3, random_lst
import random


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
    for i in range(100):
        # Supondo que temos uma função `random_jogadores` que gera uma lista de objetos Jogador aleatórios
        lst = random_jogadores(1000)
        assert quicksort(lst, 0, 1000 - 1) == sorted(lst, key=lambda jogador: jogador.media_global, reverse=True)

def test_insertion_sort():
    for i in range(100):
        lst = random_lst(14)
        assert insertion_sort(lst) == sorted(lst)

def test_merge_sort():
    for i in range(10):
        lst = random_lst(1000)
        assert merge_sort_bu(lst) == sorted(lst)


