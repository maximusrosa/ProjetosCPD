from hash_table import HashTable

class NodeHT(HashTable):
    def __iter__(self):
        for index in range(self.size):
            for item in self.table[index]:
                yield item

    def hash(self, id: str):
        return ord(id[0]) % self.size

    def insert(self, object):
        index = self.hash(object[0])
        self.table[index].append(object)

    def get(self, id: str):
        index = self.hash(id)
        for object in self.table[index]:
            if object[0] == id:  # Corrected line
                return object
        return None


class Trie:
    class Node:
        def __init__(self):
            self.children = NodeHT(5)  # floor(26 / 5) = 5
            self.player_id = None

        def __repr__(self):
            return f"{self.children} {self.player_id}"

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
            found = current.children.get(letter)

            if found:
                current = found[1]

            else:
                new_node = Trie.Node()
                current.children.insert((letter, new_node))
                current = new_node

        current.player_id = player_id

    def search(self, name: str) -> str:
        """
        Returns the player's id if his name is in the trie.
        """
        current = self.root

        for letter in name:
            found = current.children.get(letter)

            if found:
                current = found[1]

            else:
                return None

        return current.player_id

    def starts_with(self, prefix: str) -> list:
        """
        Returns all player id's that start with the given prefix.
        """
        current = self.root

        for letter in prefix:
            found = current.children.get(letter)

            if found:
                current = found[1]

            else:
                return []

        return self._get_all_player_ids(current)

    def _get_all_player_ids(self, node: "Trie.Node") -> list:
        player_ids = []

        if node.player_id is not None:
            player_ids.append(node.player_id)

        for child in node.children:
            player_ids += self._get_all_player_ids(child[1])

        return player_ids


def main():
    trie = Trie()

    jogadores = ["Alex", "Max", "Angelo", "Thiago", "Fernando", "Mateus", "Neymar", "Marcelo"]

    for i, jogador in enumerate(jogadores):
        trie.insert(jogador, i)

    print(trie.starts_with("Ma"))


if __name__ == "__main__":
    main()
