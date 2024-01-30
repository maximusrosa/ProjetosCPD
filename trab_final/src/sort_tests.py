import unittest
from hash_table import Jogador
from sort import quicksort, insertion_sort, merge_sort, _quicksort
from random import randint


class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        players = [Jogador(id=str(i), nome_curto='player' + str(i), nome_longo='player' + str(i), posicoes='M',
                           nacionalidade='Brazil', clube='Club' + str(i), liga='League' + str(i)) for i in range(10)]
        for player in players:
            player.media_global = randint(1, 100) - int(player.id)

        sorted_players = _quicksort(players, 0, len(players) - 1)
        self.assertEqual(sorted_players, sorted(players, key=lambda x: x.media_global, reverse=True))


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        players = [Jogador(id=str(i), nome_curto='player' + str(i), nome_longo='player' + str(i), posicoes='M',
                           nacionalidade='Brazil', clube='Club' + str(i), liga='League' + str(i)) for i in range(10)]
        for player in players:
            player.media_global = randint(1, 100) - int(player.id)

        sorted_players = insertion_sort(players)
        self.assertEqual(sorted_players, sorted(players, key=lambda x: x.media_global, reverse=True))

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        tuples = [(randint(0,5), Jogador(id=str(i), nome_curto='player' + str(i), nome_longo='player' + str(i), posicoes='M',
                           nacionalidade='Brazil', clube='Club' + str(i), liga='League' + str(i))) for i in range(10)]
        for tuple in tuples:
            tuple[0].media_global = randint(1, 100) - int(tuple[0].id)

        sorted_players = merge_sort(tuples)
        self.assertEqual(sorted_players, sorted(tuples, key=lambda x: (x[1], x[0].media_global), reverse=True))
        
if __name__ == '__main__':
    unittest.main()
