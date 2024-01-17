import unittest
from trie_tree import Trie

class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_word_insertion_and_search(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.search("hell"))

    def test_prefix_search(self):
        self.trie.insert("world")
        self.assertTrue(self.trie.startsWith("wor"))
        self.assertFalse(self.trie.startsWith("woa"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.startsWith(""))

    def test_non_existent_word_search(self):
        self.assertFalse(self.trie.search("nonexistent"))

    def test_non_existent_prefix_search(self):
        self.assertFalse(self.trie.startsWith("nonexistent"))