from src.hash_table import Jogador, Usuario, Tag, HashTable, TagHT
from src.trie_tree import Trie
from time import time
import csv
from math import floor
from src.sort import quicksort, merge_sort

# Constantes
NUM_JOGADORES = 18944
#NUM_USUARIOS = 9642  # pro minirating de 10k
# NUM_USUARIOS = 138425  # pro rating de 1M
NUM_USUARIOS = 138493  # pro rating de 10M / 24M
NUM_TAGS = 937


class FIFA_Database:
    def __init__(self):
        self.players_HT = HashTable(floor(NUM_JOGADORES / 5))
        self.users_HT = HashTable(floor(NUM_USUARIOS / 5))
        self.tags_HT = TagHT(floor(NUM_TAGS / 5))
        self.long_names_Trie = Trie()

    # ----------------------------------------- Pré-processamento ----------------------------------------- #

    def get_players_info(self, filename='data/players.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                self.players_HT.insert(Jogador(id=row[0], nome_curto=row[1], nome_longo=row[2], posicoes=row[3],
                                               nacionalidade=row[4], clube=row[5], liga=row[6]))
                self.long_names_Trie.insert(row[2], row[0])

        print("Tabela Hash de jogadores e Árvore Trie de nomes longos construídas.")

    def get_rating_info(self, filename='data/rating.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            lastIdChecked = None  # responsável por saber qual último sofifa_id visitado

            print("\nConstruindo Tabela Hash de usuários...\n")

            for row in reader:
                user_id = row[0]
                sofifa_id = row[1]
                rating = float(row[2])

                if lastIdChecked != sofifa_id:
                    lastIdChecked = sofifa_id

                    player = self.players_HT.get(sofifa_id)
                    player.soma_notas += rating
                    player.num_avaliacoes += 1

                else:
                    player.soma_notas += rating
                    player.num_avaliacoes += 1

                user = self.users_HT.get(user_id)

                if user is None:
                    self.users_HT.insert(Usuario(user_id, [(sofifa_id, rating)]))
                else:
                    user.avaliacoes.append((sofifa_id, rating))

        print("Tabela Hash de usuários construída.")

        self._update_global_ratings()
        print("Médias globais atualizadas.")

    def get_tags_info(self, filename='data/tags.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                tag = self.tags_HT.get(row[2])

                if tag is None:
                    self.tags_HT.insert(Tag(id=row[2], ocorrencias={row[1]}))
                else:
                    tag.ocorrencias.add(row[1])

        print("Tabela Hash de Tags construída.")

    def _update_global_ratings(self):
        for lista in self.players_HT.table:
            for jogador in lista:
                if jogador.num_avaliacoes != 0:
                    jogador.media_global = round((jogador.soma_notas / jogador.num_avaliacoes), 6)

    # ----------------------------------------- Pesquisas ----------------------------------------- #

    def top_by_prefix(self, prefix):
        # Create a list of players with the given prefix
        players = [self.players_HT.get(id)
                   for id in self.long_names_Trie.starts_with(prefix)]

        # Sort the list of players by their global average
        return quicksort(players)

    def top_by_tags(self, tags):
        # Create a set of all player ids that have all the tags
        player_ids = set.intersection(*[self.tags_HT.get(tag).ocorrencias
                                        for tag in tags])

        # Create a list of players with the given ids
        players = [self.players_HT.get(player_id)
                   for player_id in player_ids]

        # Sort the list of players by their global average
        return quicksort(players)

    def top_by_position(self, n, position):
        players = [jogador for lista in self.players_HT.table for jogador in lista
                                if position in jogador.posicoes and jogador.num_avaliacoes > 1000]

        return quicksort(players)[:n]

    def top_by_user(self, user_id):
        user = self.users_HT.get(user_id)

        # Crie uma lista de tuplas (Jogador, rating) com as avaliações do usuário
        tuplas = [(self.players_HT.get(sofifa_id), rating) for sofifa_id, rating in user.avaliacoes]

        return merge_sort(tuplas)[:20]

    
    def top_by_club(self, club):
        players = [jogador for lista in self.players_HT.table for jogador in lista
                                if club == jogador.clube and jogador.num_avaliacoes > 1000]

        return quicksort(players)
    
    def top_by_nationality(self, nationality):
        players = [jogador for lista in self.players_HT.table for jogador in lista
                                if nationality == jogador.nacionalidade and jogador.num_avaliacoes > 1000]
        
        return quicksort(players)
    
    def top_by_league(self, league):
        players = [jogador for lista in self.players_HT.table for jogador in lista
                                if league == jogador.liga and jogador.num_avaliacoes > 1000]
        
        return quicksort(players)


# ----------------------------------------- Funções auxiliares ----------------------------------------- #

def find_user_with_most_reviews(hash_table):
    max_reviews = 0
    user_with_most_reviews = None

    # Percorre todas as listas na tabela hash
    for user_list in hash_table.table:
        # Percorre todos os usuários em cada lista
        for user in user_list:
            # Se o usuário atual tem mais avaliações do que o máximo atual
            if len(user.avaliacoes) > max_reviews:
                # Atualiza o máximo e o usuário com mais avaliações
                max_reviews = len(user.avaliacoes)
                user_with_most_reviews = user

    return user_with_most_reviews


def count_unique_tags(filename='data/tags.csv'):
    unique_tags = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            unique_tags.add(row[2])  # The tag is in the third column

    return len(unique_tags)


def count_unique_users(filename='data/rating.csv'):
    unique_users = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            unique_users.add(row[0])  # The user id is in the first column

    return len(unique_users)


# --------------------------------------------------------------------------------------------------------- #

def main():
    # Estruturas
    start = time()

    fifa_db = FIFA_Database()

    fifa_db.get_players_info()

    fifa_db.get_tags_info()

    fifa_db.get_rating_info('data/rating.csv')

    end = time()

    print(
        f'\nTempo de construção das estruturas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos\n')

    # Consultas
    print("20 jogadores mais bem avaliados pelo usuário '106180':")
    for player, rating in fifa_db.top_by_user('106180'):
        print(f"{player}, {rating}")



if __name__ == '__main__':
    main()
