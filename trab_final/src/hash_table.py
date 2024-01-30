from typing import NamedTuple


class Jogador:
    def __init__(self, id, nome_curto, nome_longo, posicoes, nacionalidade, clube, liga):
        self.id = id
        self.nome_curto = nome_curto
        self.nome_longo = nome_longo
        self.posicoes = posicoes
        self.nacionalidade = nacionalidade
        self.clube = clube
        self.liga = liga

        self.soma_notas = self.num_avaliacoes = self.media_global = 0

    def __str__(self):
        return f'({self.id}, {self.nome_curto}, {self.nome_longo}, {self.posicoes}, {self.nacionalidade}, {self.clube}, {self.liga}, {self.media_global})'


class Usuario(NamedTuple):
    id: str
    avaliacoes: list[tuple[str, float]]

    def __str__(self):
        return f'(user_id: {self.id}, ratings: {self.avaliacoes})'


class Tag(NamedTuple):
    id: str  # Nome da tag
    ocorrencias: set[str]  # ID dos jogadores que possuem essa tag

    def __str__(self):
        return f'(tag: {self.id}, ocorrencias: {self.ocorrencias})'


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
        return int(id) % self.size

    def _resize(self):
        #print('Redimensionando a tabela hash...')
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]

        for bucket in self.table:
            for _ in bucket:
                index = self.hash(_.id[0])
                new_table[index].append(_)

        self.table = new_table
        del new_table

    def insert(self, object):
        index = self.hash(object.id)
        self.table[index].append(object)

    def get(self, id: str):
        index = self.hash(id)

        for object in self.table[index]:
            if object.id == id:
                return object

        return None

    # ----------------------------------------- ESTATÍSTICAS ----------------------------------------- #

    def _average_list_size(self):
        soma = 0
        contador = 0

        for lista in self.table:
            if lista:  # se a lista não estiver vazia
                soma += len(lista)
                contador += 1

        media = soma / contador if contador != 0 else 0

        return media

    def cons_stats(self):
        # calcula a média do tamanho das listas não vazias
        media = self._average_list_size()

        # maior tamanho de lista
        tamanho_max = max([len(lista) for lista in self.table])

        # conta o número de posições do "array" com listas não vazias
        posicoes_ocupadas = 0

        for lista in self.table:
            if lista:
                posicoes_ocupadas += 1

        print(f'ESTATISTICAS DA TABELA HASH\n'
              f'Taxa de ocupacao: {(posicoes_ocupadas / self.size) * 100:.2f}%\n'
              f'Tamanho maximo de lista: {tamanho_max:.0f} elementos\n'
              f'Tamanho medio de lista: {media:.3f} elementos\n')


class TagHT(HashTable):
    # Método de Horner
    def hash(self, id: str) -> int:
        hash_value = 0

        for char in id:
            hash_value = ord(char) + (31 * hash_value)

        return hash_value % self.size

