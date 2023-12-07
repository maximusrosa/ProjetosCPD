class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return ord(key[0]) % self.size

    def set(self, key, value):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                kvp[1] = value
                return

        self.table[hash_index].append([key, value])

    def get(self, key):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError(f'Key {key} not found')

    def remove(self, key):
        hash_index = self._hash(key)
        for i, kvp in enumerate(self.table[hash_index]):
            if kvp[0] == key:
                self.table[hash_index].pop(i)
                return

        raise KeyError(f'Key {key} not found')


def main():
    # Create a hash table of size 10
    hash_table = HashTable(10)

    # Set some values
    hash_table.set('a1', 1)
    hash_table.set('a2', 1)
    hash_table.set('b', 2)
    hash_table.set('c', 3)
    hash_table.set('d', 4)

    # Get some values
    print(hash_table.get('a1'))
    print(hash_table.get('a2'))
    print(hash_table.get('b'))
    print(hash_table.get('c'))


if __name__ == '__main__':
    main()
