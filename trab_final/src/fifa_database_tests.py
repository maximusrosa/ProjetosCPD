import unittest
from fifa_database import FIFA_Database

ID_USER_MAX_REVIEWS = '130642'

class TestFIFADatabase(unittest.TestCase):
    def setUp(self):
        self.fifa_db = FIFA_Database()

    # Procurando o Messi
    def test_get_players_info(self):
        self.fifa_db.get_players_info()
        assert str(self.fifa_db.players_HT.get("158023")) == '(158023, L. Messi, RW, ST, CF, Argentina, FC Barcelona, Spain Primera Division, 0.000000)'

    # Pesquisa 2: jogadores revisados por usuários
    def test_top_by_user(self):
        self.fifa_db.get_players_info()
        self.fifa_db.get_minirating_info("../data/minirating.csv")
        self.fifa_db.update_global_ratings()

        top_rated_players = self.fifa_db.top_by_user(ID_USER_MAX_REVIEWS)
        assert top_rated_players == [('229683', 4.0, 4.0), ('252270', 4.0, 4.0), ('240600', 3.5, 2.5), ('207768', 2.5, 2.5)]

    # Pesquisa 3: melhores jogadores de uma determinada posição
    def test_top_by_position(self):
        self.fifa_db.get_players_info()
        self.fifa_db.get_minirating_info("../data/minirating.csv")
        self.fifa_db.update_global_ratings()

        top_players = self.fifa_db.top_by_position("ST", 6)
        assert top_players == [('215061', 5.0), ('143001', 5.0), ('200647', 5.0), ('176580', 5.0), ('211300', 5.0), ('183277', 4.833333333333333)]


if __name__ == '__main__':
    unittest.main()
