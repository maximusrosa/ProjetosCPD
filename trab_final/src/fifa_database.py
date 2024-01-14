from hash_table import HashTable, Jogador, Usuario, Tag
from trie_tree import Trie
from time import time
import csv

# Constantes
NUM_JOGADORES = 18944
NUM_USUARIOS = 9642  # pro minirating de 10k
NUM_TAGS = 937

ID_USER_MAX = '130642'  # id do usuário com mais avaliações

class FIFA_Database:
    def __init__(self):
        # O tamanho foi escolhido como o número primo mais próximo de floor(NUM_OBJETOS + (0.2 * NUM_OBJETOS))
        self.players_HT = HashTable(22739)
        self.users_HT = HashTable(11579)
        self.tags_HT = HashTable(1129)
        #self.nomes_Trie = Trie()

    def __str__(self):
        return str(self.players_HT) + '\n' + str(self.users_HT)

    # ----------------------------------------- Pré-processamento ----------------------------------------- #

    def get_players_info(self, filename='../data/players.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            for row in reader:
                self.players_HT.insert(Jogador(id=row[0], nome_curto=row[1], nome=row[2], posicoes=row[3],
                                               nacionalidade=row[4], clube=row[5], liga=row[6]))

    def get_minirating_info(self, filename='../data/minirating.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Atualização da Tabela de Usuários
                user = self.users_HT.get(row[0])

                if user is None:
                    self.users_HT.insert(Usuario(id=row[0], avaliacoes=[Usuario.Avaliacao(player_id=row[1], nota=float(row[2]))]))
                else:
                    user.avaliacoes.append(Usuario.Avaliacao(player_id=row[1], nota=float(row[2])))

                # Atualização da Tabela de Jogadores
                index = self.players_HT.hash(row[1])

                for jogador in self.players_HT.table[index]:
                    if jogador.id == row[1]:
                        jogador.soma_notas += float(row[2])
                        jogador.num_avaliacoes += 1

    def get_tags_info(self, filename='../data/tags.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Atualização da Tabela de Tags
                tag = self.tags_HT.get(row[2])

                if tag is None:
                    self.tags_HT.insert(Tag(id=row[2], ocorrencias={self.players_HT.get(row[1])}))
                else:
                    tag.ocorrencias.add(self.players_HT.get(row[1]))


    def update_global_ratings(self):
        start = time()

        for lista in self.players_HT.table:
            for jogador in lista:
                if jogador.num_avaliacoes != 0:
                    jogador.media_global = jogador.soma_notas / jogador.num_avaliacoes

        end = time()
        print(f'Tempo para atualizar as médias globais: {(end - start) * 1000:.4f} milisegundos')

    # ----------------------------------------- Pesquisas ----------------------------------------- #

    def top_by_user(self, user_id):
        user = self.users_HT.get(user_id)

        # Create a list of tuples containing the player's id, the user's rating and the player's global average
        top_rated_players = [
            (avaliacao.player_id, avaliacao.nota, self.players_HT.get(avaliacao.player_id).media_global)
            for avaliacao in user.avaliacoes]

        # Sort the list in descending order by user_rating and then by global_average
        top_rated_players.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Esta pesquisa deve retornar a lista com no máximo 20 jogadores revisados pelo usuário
        return str(top_rated_players[:20])

    def top_by_position(self, position, n):
        top_players = [(jogador.id, jogador.media_global)
                       for lista in self.players_HT.table for jogador in lista
                       if position in jogador.posicoes and jogador.num_avaliacoes > 0]

        top_players.sort(key=lambda x: x[1], reverse=True)

        return top_players[:n]


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

def count_unique_users(filename='../data/minirating.csv'):
    unique_users = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            unique_users.add(row[0])  # The user id is in the first column

    return len(unique_users)

# ----------------------------------------- Testes ----------------------------------------- #

def main():
    fifa_db = FIFA_Database()

    start = time()
    fifa_db.get_players_info()
    fifa_db.get_minirating_info("../data/minirating.csv")
    fifa_db.get_tags_info()
    fifa_db.update_global_ratings()
    end = time()

    print(f'Tempo de construção das tabelas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')

    # Ex: Procurando o Messi
    print(str(fifa_db.players_HT.get("158023")))

    # Pesquisa 2: jogadores revisados por usuários
    print(fifa_db.top_by_user(ID_USER_MAX))

    # Pesquisa 3: melhores jogadores de uma determinada posição
    print(fifa_db.top_by_position("ST", 6))

    # Salvando os tabelas
    with open('../output/players_ht.txt', 'w') as file:
        file.write(str(fifa_db.players_HT))

    with open('../output/users_ht.txt', 'w') as file:
        file.write(str(fifa_db.users_HT))

    with open('../output/tags_ht.txt', 'w') as file:
        file.write(str(fifa_db.tags_HT))


if __name__ == '__main__':
    main()