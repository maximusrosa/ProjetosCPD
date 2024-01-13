class Trie:
    class Node:
        def __init__(self):
            self.children = {}  # ver com o sor se realmente podemos usar um dicionário aqui
            self.is_word = False

        def __str__(self):
            return f'({self.children}, {self.is_word})'

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = self.Node()
            node = node.children[c]

        node.is_word = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

    def get_words(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        return self._get_words(node, prefix)

    def _get_words(self, node, prefix):
        words = []
        if node.is_word:
            words.append(prefix)

        for c in node.children:
            words += self._get_words(node.children[c], prefix + c)

        return words


def main():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("helium")
    print(trie)



if __name__ == "__main__":
    main()
