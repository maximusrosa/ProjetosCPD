from collections import namedtuple
import csv

ParChaveValor = namedtuple('ParChaveValor', ['id', 'chave', 'valor'])

class HashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0  # Adiciona um contador para acompanhar o número de elementos
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(caractere) for caractere in key) % self.size  # Ex: 'Thiago' -> 'Thi' -> 293 % 10 = 3

    def insert(self, id, key, value):
        if self.count / self.size > 0.7: # Se a taxa de ocupação é maior que 70%
            self._resize()  # Redimensiona a tabela hash

        variavel = key[0:3]  # Pega as três primeiras letras do nome como chave
        hash_index = self._hash(variavel)
        
        #for par in self.table[hash_index]:                      ################################### Nem precisa disso
         #   if par.chave == key:
          #      print(f"Nome {key} já está na tabela")
           #     return                                          ################################### Nem precisa disso

        self.count += 1
        self.table[hash_index].append(ParChaveValor(id, key, value))

    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]
        for bucket in self.table:
            for par in bucket:
                hash_index = self._hash(par.chave[0])
                new_table[hash_index].append(par)
        self.table = new_table


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
                output += ", ".join([f"({par.id}, {par.chave}, {par.valor})" for par in par_list])
            output += "\n"
        return output


def main():
    hash_table = HashTable(10)

    with open('players.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        for i, row in enumerate(reader):
            if i >= 100:
                break
            id = row[0]
            key = row[1]
            value = row[2:]

            hash_table.insert(id, key, value)

    print(hash_table)


if __name__ == '__main__':
    main()
