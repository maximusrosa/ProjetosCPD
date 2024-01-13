from typing import NamedTuple

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
        return f'({self.id}, {self.nome_curto}, {self.posicoes}, {self.nacionalidade}, {self.clube}, {self.liga}, {self.media_global:.6f})'


class Usuario(NamedTuple):
    class Avaliacao(NamedTuple):
        player_id: str
        nota: float

        def __str__(self):
            return f'(player_id: {self.player_id}, nota: {self.nota})'

    id: str
    avaliacoes: list[Avaliacao]

    def __str__(self):
        return f'(user_id: {self.id}, ratings: {self.avaliacoes})'

class Tag(NamedTuple):
    id: str  # Nome da tag
    ocorrencias: set[Jogador]  # ver com o sor se realmente podemos usar um conjunto aqui

    def __str__(self):
        return f'(tag: {self.id}, ocorrencias: {[jogador.nome_curto for jogador in self.ocorrencias]})'

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
        hash_value = 5381
        for char in id:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash * 33 + c

        return hash_value % self.size

    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]

        for bucket in self.table:
            for _ in bucket:
                index = self.hash(_.id[0])
                new_table[index].append(_)

        self.table = new_table
        del new_table

    def insert(self, object: Jogador | Usuario | Tag):
        index = self.hash(object.id)
        self.table[index].append(object)

        # Se a taxa de ocupação dessa lista encadeada é maior que 20% do tamanho da tabela hash
        if len(self.table[index]) / self.size > 0.2:
            self._resize()  # Redimensiona a tabela hash

    def get(self, id: str) -> Jogador | Usuario | Tag | None:
        index = self.hash(id)

        for object in self.table[index]:
            if object.id == id:
                return object

        return None
