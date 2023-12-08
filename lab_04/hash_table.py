from collections import namedtuple
import csv

ParChaveValor = namedtuple('ParChaveValor', ['chave', 'valor'])

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return ord(key[0]) % self.size            #Ex: 'Thiago' -> 'T' -> 84 % 10 = 4

    def insert(self, key, value):
        hash_index = self._hash(key)
        for par in self.table[hash_index]:
            if par.chave == key:
                par.valor = value
                return

        self.table[hash_index].append(ParChaveValor(key, value))

    def get(self, key):
        hash_index = self._hash(key)
        for par in self.table[hash_index]:
            if par.chave == key:
                return par.valor

        raise KeyError(f'Key {key} not found')

    def remove(self, key):
        hash_index = self._hash(key)
        for i, par in enumerate(self.table[hash_index]):
            if par.chave == key:
                self.table[hash_index].pop(i)
                return

        raise KeyError(f'Key {key} not found')
    
    def __str__(self):
        output = ""
        for i, par_list in enumerate(self.table):
            output += f"{i}: "
            if par_list:
                output += ", ".join([f"({par.chave}, {par.valor})" for par in par_list])
            output += "\n"
        return output 


def main():
    hash_table = HashTable(10)


    with open('players.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        for i, row in enumerate(reader):
            if i >= 20:
                break
            key = row[0]  # Supondo que a chave seja a primeira coluna
            value = row[1:]  # E o valor seja o restante da linha
            hash_table.insert(key, value)


    print(hash_table)

if __name__ == '__main__':
    main()
