from hash_table import Jogador, Usuario, Tag, JogadorHT, UsuarioHT, TagHT
from trie_tree import Trie
from time import time
import csv
from collections import defaultdict
from math import floor, ceil

# Constantes
NUM_JOGADORES = 18944
#NUM_USUARIOS = 138425  # pro rating de 1M
NUM_USUARIOS = 138493  # pro rating de 10M
#NUM_USUARIOS = 138493  # pro rating de 24M
NUM_TAGS = 937


class FIFA_Database:
    def __init__(self):
        self.players_HT = JogadorHT(floor(NUM_JOGADORES / 5))
        self.users_HT = UsuarioHT(floor(NUM_USUARIOS / 5))
        self.tags_HT = TagHT(floor(NUM_TAGS / 5))
        self.long_names_Trie = Trie()

    def __str__(self):
        return str(self.players_HT) + '\n' + str(self.users_HT) + '\n' + str(self.tags_HT) + '\n' + str(
            self.long_names_Trie)

    # ----------------------------------------- Pré-processamento ----------------------------------------- #

    def get_players_info(self, filename='../data/players.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            for row in reader:
                self.players_HT.insert(Jogador(id=row[0], nome_curto=row[1], nome=row[2], posicoes=row[3],
                                               nacionalidade=row[4], clube=row[5], liga=row[6]))
                # self.long_names_Trie.insert(row[2], row[0])

    def get_minirating_info(self, filename='../data/minirating.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            print("\nConstruindo Tabela Hash de Usuários...\n")

            for row in reader:
                #user_id = row[0]
                #sofifa_id = row[1]
                #rating = float(row[2])
                
                # Atualização da Tabela de Usuários
                if self.users_HT.get(row[0]) is not None:
                    self.users_HT.get(row[0]).avaliacoes.append(Usuario.Avaliacao(row[1], float(row[2])))

                else:
                    self.users_HT.insert(Usuario(row[0], [Usuario.Avaliacao(row[1], float(row[2]))]))

                # Atualização da Tabela de Jogadores
                index = self.players_HT.hash(row[1])

                for jogador in self.players_HT.table[index]:
                    if jogador.id == row[1]:
                        jogador.soma_notas += float(row[2])
                        jogador.num_avaliacoes += 1

        print("Tabela Hash de Usuários construída.")

        self._update_global_ratings()
        print("Médias globais atualizadas.")

    def get_tags_info(self, filename='../data/tags.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Atualização da Tabela de Tags
                tag = self.tags_HT.get(row[2])

                if tag is None:
                    self.tags_HT.insert(Tag(id=row[2], ocorrencias={row[1]}))
                else:
                    tag.ocorrencias.add(row[1])

    def _update_global_ratings(self):
        # start = time()

        for lista in self.players_HT.table:
            for jogador in lista:
                if jogador.num_avaliacoes != 0:
                    jogador.media_global = jogador.soma_notas / jogador.num_avaliacoes

        # end = time()
        # print(f'Tempo para atualizar as médias globais: {(end - start) * 1000:.4f} milisegundos')

    # ----------------------------------------- Pesquisas ----------------------------------------- #

    def players_by_prefix(self, prefix):
        players = [self.players_HT.get(id)
                   for id in self.long_names_Trie.starts_with(prefix)]

        # Sort the list of players by their global average
        players.sort(key=lambda x: x.media_global, reverse=True)

        return players

    def top_by_user(self, user_id):
        user = self.users_HT.get(user_id)

        # Create a list of tuples containing the player's id, the user's rating and the player's global average
        top_rated_players = [
            (avaliacao.player_id, avaliacao.nota, self.players_HT.get(avaliacao.player_id).media_global)
            for avaliacao in user.avaliacoes]

        # Sort the list in descending order by user_rating and then by global_average
        top_rated_players.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Esta pesquisa deve retornar a lista com no máximo 20 jogadores revisados pelo usuário
        return top_rated_players[:20]

    def top_by_position(self, n, position):
        top_players = [(jogador.id, jogador.media_global)
                       for lista in self.players_HT.table for jogador in lista
                       if position in jogador.posicoes and jogador.num_avaliacoes > 0]

        top_players.sort(key=lambda x: x[1], reverse=True)

        return top_players[:n]

    def players_by_tags(self, tags):
        # Create a set of all player ids that have all the tags
        player_ids = set.intersection(*[self.tags_HT.get(tag).ocorrencias
                                        for tag in tags])

        # Create a list of players with the given ids
        players = [self.players_HT.get(player_id)
                   for player_id in player_ids]

        # Sort the list of players by their global average
        players.sort(key=lambda x: x.media_global, reverse=True)

        return players


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


def count_unique_tags(filename='../data/tags.csv'):
    unique_tags = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            unique_tags.add(row[2])  # The tag is in the third column

    return len(unique_tags)


def count_unique_users(filename='../data/rating.csv'):
    unique_users = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            unique_users.add(row[0])  # The user id is in the first column

    return len(unique_users)


# --------------------------------------------------------------------------------------------------------- #

def main():
    # Pré-processamento
    fifa_db = FIFA_Database()

    start = time()

    fifa_db.get_players_info()
    print("Tabela Hash de jogadores construída.")

    fifa_db.get_minirating_info('../data/rating_10m.csv')  # Boss Final

    # fifa_db.get_tags_info()
    # print("Tabela Hash de Tags construída.")

    end = time()

    print(
        f'Tempo de construção das estruturas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos\n')

    # Testando as funções hash / tamanho das tabelas
    # fifa_db.players_HT.cons_stats()
    fifa_db.users_HT.cons_stats()
    # fifa_db.tags_HT.cons_stats()

    # Salvando os tabelas
    # with open('../output/players_ht.txt', 'w') as file:
    # file.write(str(fifa_db.players_HT))

    #with open('../output/users_ht.txt', 'w') as file:
        #file.write(str(fifa_db.users_HT))

    # with open('../output/tags_ht.txt', 'w') as file:
    # file.write(str(fifa_db.tags_HT))


if __name__ == '__main__':
    main()
