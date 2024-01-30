from src.hash_table import HashTable
from typing import NamedTuple

class EdgeHT(HashTable):
    def __iter__(self):
        for index in range(self.size):
            for item in self.table[index]:
                yield item

    def hash(self, id: str):
        return ord(id) % self.size

    def insert(self, object):
        index = self.hash(object.id)
        self.table[index].append(object)

        # Se a taxa de ocupação dessa lista encadeada é maior que 20% do tamanho da tabela hash
        if len(self.table[index]) / self.size > 0.2:
            self._resize()  # Redimensiona a tabela hash

class Trie:
    class Node:
        class Edge(NamedTuple):
            id: str  # Letra
            node: "Trie.Node"

        def __init__(self):
            self.edges = EdgeHT(5)  # floor(26 / 5) = 5
            self.player_id = None

        def __repr__(self):
            return f"{self.edges} {self.player_id}"


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.Node()

    def __str__(self):
        return str(self.root)

    def insert(self, name: str, player_id: str) -> None:
        """
        Inserts a name into the trie.
        """
        current = self.root

        for letter in name:
            found = current.edges.get(letter)

            if found:
                current = found.node

            else:
                new_node = Trie.Node()
                current.edges.insert(Trie.Node.Edge(letter, new_node))
                current = new_node

        current.player_id = player_id

    def search(self, name: str) -> str:
        """
        Returns the player's id if his name is in the trie.
        """
        current = self.root

        for letter in name:
            found = current.edges.get(letter)

            if found:
                current = found.node

            else:
                return None

        return current.player_id

    def starts_with(self, prefix: str) -> list:
        """
        Returns all player id's that start with the given prefix.
        """
        current = self.root

        for letter in prefix:
            found = current.edges.get(letter)

            if found:
                current = found.node

            else:
                return []

        return self._get_all_player_ids(current)

    def _get_all_player_ids(self, node: "Trie.Node") -> list:
        player_ids = []

        if node.player_id is not None:
            player_ids.append(node.player_id)

        for edge in node.edges:
            player_ids += self._get_all_player_ids(edge.node)

        return player_ids


def main():
    trie = Trie()

    jogadores = ["Alex", "Max", "Angelo", "Thiago", "Fernando", "Mateus", "Neymar", "Marcelo"]

    for i, jogador in enumerate(jogadores):
        trie.insert(jogador, i)

    print(trie.starts_with("Ma"))


if __name__ == "__main__":
    main()
