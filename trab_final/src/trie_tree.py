class Trie:
    class Node:
        def __init__(self):
            self.children = []  # Now each child is a tuple (letter, node)
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
            found = False

            for child_letter, child_node in current.children:
                if child_letter == letter:
                    current = child_node
                    found = True
                    break

            if not found:
                new_node = Trie.Node()
                current.children.append((letter, new_node))  # Append a tuple
                current = new_node

        current.player_id = player_id

    def search(self, name: str) -> str:
        """
        Returns the player's id if his name is in the trie.
        """
        current = self.root

        for letter in name:
            found = False

            for child_letter, child_node in current.children:
                if child_letter == letter:
                    current = child_node
                    found = True
                    break

            if not found:
                return None

        return current.player_id

    def starts_with(self, prefix: str) -> list:
        """
        Returns all player id's that start with the given prefix.
        """
        current = self.root

        for letter in prefix:
            found = False

            for child_letter, child_node in current.children:
                if child_letter == letter:
                    current = child_node
                    found = True
                    break

            if not found:
                return []

        return self._get_all_player_ids(current)

    def _get_all_player_ids(self, node: "Trie.Node") -> list:
        player_ids = []

        if node.player_id is not None:
            player_ids.append(node.player_id)

        for child_letter, child_node in node.children:
            player_ids += self._get_all_player_ids(child_node)

        return player_ids

def main():
    trie = Trie()

    jogadores = ["Alex", "Max", "Angelo", "Thiago", "Fernando", "Mateus"]

    for i, jogador in enumerate(jogadores):
        trie.insert(jogador, i)

    print(trie.starts_with("Ma"))


if __name__ == "__main__":
    main()