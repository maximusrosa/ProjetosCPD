import csv
from time import time
from collections import namedtuple
from typing import NamedTuple

# Constantes
ID_USER_MAX = '130642'  # id do usuário com mais avaliações
TAMANHO_TABELA = 7993

Avaliacao = namedtuple('Avaliacao', ['player_id', 'nota'])

class Jogador:
    def __init__(self, id, nome_curto, nome, posicoes, nacionalidade, clube, liga):
        self.id = id
        self.nome_curto = nome_curto
        self.nome = nome
        self.posicoes = posicoes
        self.nacionalidade = nacionalidade
        self.clube = clube
        self.liga = liga

        self.soma_notas = self.num_avaliacoes = self.media_global = 0

    def __str__(self):
        return f'({self.id}, {self.nome_curto}, {self.nome}, {self.posicoes}, {self.nacionalidade}, {self.clube}, {self.liga}, {self.media_global:.6f})'


class Usuario(NamedTuple):
    id: str
    avaliacoes: list[Avaliacao]

    def __str__(self):
        return f'(user_id: {self.id}, {self.avaliacoes})'


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __str__(self):
        output = ""

        for i, lista in enumerate(self.table):
            output += f"{i}: "

            if lista:
                output += ", ".join([str(object) for object in lista])

            output += "\n"

        return output

    def hash(self, id: str) -> int:
        # lista de números primos com o 1
        numeros = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        resultado = 1

        for i, digito in enumerate(str(id)):
            # Ex: id = 357741 -> 1^3 + 2^5 + 3^7 + 5^7 + 7^4 + 11^1
            resultado += numeros[i] ** int(digito)

        return resultado % self.size

    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]

        for bucket in self.table:
            for _ in bucket:
                index = self.hash(_.id[0])
                new_table[index].append(_)

        self.table = new_table
        del new_table

    def insert(self, object: Jogador | Usuario):
        index = self.hash(object.id)
        self.table[index].append(object)

        # Se a taxa de ocupação dessa lista encadeada é maior que 20% do tamanho da tabela hash
        if len(self.table[index]) / self.size > 0.2:
            self._resize()  # Redimensiona a tabela hash

    def get(self, id):
        index = self.hash(id)

        for object in self.table[index]:
            if object.id == id:
                return object

        return None


class FIFA_Database():
    def __init__(self):
        self.players_HT = HashTable(TAMANHO_TABELA)
        self.users_HT = HashTable(TAMANHO_TABELA)
        #self.tags_ht = HashTable(TAMANHO_TABELA)

    def __str__(self):
        return str(self.players_HT) + '\n' + str(self.users_HT)

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
                index = self.players_HT.hash(row[0])

                user = self.users_HT.get(row[0])
                if user is None:
                    self.users_HT.insert(Usuario(id=row[0], avaliacoes=[Avaliacao(player_id=row[1], nota=row[2])]))
                else:
                    user.avaliacoes.append(Avaliacao(player_id=row[1], nota=row[2]))

                # Atualização da Tabela de Jogadores
                index = self.players_HT.hash(row[1])

                for jogador in self.players_HT.table[index]:
                    if jogador.id == row[1]:
                        jogador.soma_notas += float(row[2])
                        jogador.num_avaliacoes += 1

    def update_global_ratings(self):
        start = time()

        for lista in self.players_HT.table:
            for jogador in lista:
                if jogador.num_avaliacoes != 0:
                    jogador.media_global = jogador.soma_notas / jogador.num_avaliacoes

        end = time()
        print(f'Tempo para atualizar as médias globais: {(end - start) * 1000:.4f} milisegundos')


    def find_user_with_most_reviews(self):
        max_reviews = 0
        user_with_most_reviews = None

        # Percorre todas as listas na tabela hash
        for user_list in self.users_HT.table:
            # Percorre todos os usuários em cada lista
            for user in user_list:
                # Se o usuário atual tem mais avaliações do que o máximo atual
                if len(user.avaliacoes) > max_reviews:
                    # Atualiza o máximo e o usuário com mais avaliações
                    max_reviews = len(user.avaliacoes)
                    user_with_most_reviews = user

        return user_with_most_reviews

    def top_by_user(self, user_id):
        user = self.users_HT.get(user_id)

        # Create a list of tuples containing the player's id, the user's rating and the player's global average
        top_rated_players = [(avaliacao.player_id, avaliacao.nota, self.players_HT.get(avaliacao.player_id).media_global)
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

def main():
    fifa_db = FIFA_Database()

    start = time()
    fifa_db.get_players_info()
    fifa_db.get_minirating_info()
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


if __name__ == '__main__':
    main()
