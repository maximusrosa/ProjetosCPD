from collections import namedtuple
import csv
from time import time

Jogador = namedtuple('Jogador', ['id', 'nome', 'posições'])


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, id):
        # lista de números primos com o 1
        numeros = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        resultado = 1
        for i, digito in enumerate(str(id)):
            # Ex: id = 357741 -> 1^3 + 2^5 + 3^7 + 5^7 + 7^4 + 11^1
            resultado += numeros[i] ** int(digito)
        return resultado % self.size
    
    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]
        for bucket in self.table:
            for jogador in bucket:
                hash_index = self._hash(jogador.id[0])
                new_table[hash_index].append(jogador)
        self.table = new_table

    def insert(self, id, key, value):

        hash_index = self._hash(id)

        self.table[hash_index].append(Jogador(id, key, value))

        # Se a taxa de ocupação de uma das listas encadeadas é maior que 70%
        # if len(self.table[hash_index]) / self.size > 0.7:
        #   self._resize()  # Redimensiona a tabela hash

    def get(self, id):
        consultas = 0
        hash_index = self._hash(id)
        for jogador in self.table[hash_index]:
            consultas += 1
            if jogador.id == id:
                return (f"{id}", f"{jogador.nome_longo}", consultas)
        return (f"{id}", "NAO ENCONTRADO", consultas)

    def remove(self, id):
        hash_index = self._hash(id)
        for i, jogador in enumerate(self.table[hash_index]):
            print(f"nome: {jogador.id}")
            if jogador.id == id:
                self.table[hash_index].pop(i)
                return

    def __str__(self):
        output = ""
        for i, lista_jogadores in enumerate(self.table):
            output += f"{i}: "
            if lista_jogadores:
                output += ", ".join(
                    [f"({jogador.id}, {jogador.nome_longo}, {jogador.posições})" for jogador in lista_jogadores])
            output += "\n"
        return output

    def média_ocupação(self):
        soma = 0
        contador = 0
        for lista in self.table:
            if lista:  # se a lista não estiver vazia
                soma += len(lista)
                contador += 1
        media = soma / contador if contador != 0 else 0
        return media


def cria_tabela(tamanho):
    hash_table = HashTable(tamanho)

    with open('players.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho

        # pega o tempo de construção da tabela
        start = time()

        # mermão tem bruxaria aqui, se apagar esse i o código não funciona
        for i, row in enumerate(reader):
            id = row[0]
            key = row[1]
            value = row[2:]

            hash_table.insert(id, key, value)  # insere na tabela

        end = time()

        # calcula a média do tamanho das listas não vazias
        media = hash_table.média_ocupação()

        # maior tamanho de lista
        tamanho_max = max([len(lista) for lista in hash_table.table])

        posicoes_ocupadas = 0

        for lista in hash_table.table:
            if lista:  # se a lista não estiver vazia
                posicoes_ocupadas += 1

        # salva num arquivo o tempo de construção em milisegundos
        with open(f'experimento{tamanho}.txt', 'w') as file:
            file.write(f'Parte 1: ESTATISTICAS DA TABELA HASH\n'
                       f'Tempo de construcao da tabela: {end - start:.5f} segundos ou {(end - start)*1000:.5f} milisegundos\n'
                       f'Taxa de ocupacao: {(posicoes_ocupadas/tamanho) * 100:.2f}%\n'
                       f'Tamanho maximo de lista: {tamanho_max:.0f} elementos\n'
                       f'Tamanho medio de lista: {media:.1f} elementos\n\n')

    return hash_table


def estatisticas_consultas(hash_table, tamanho):

    with open(f'consultas.csv', 'r') as file:
        reader = list(csv.reader(file))

        lista_de_tuplas = [None] * len(reader)

        start = time()

        for i, row in enumerate(reader):
            id = row[0]

            # retorna uma tupla com o (id, nome, num_consultas) mas nome = NAO ENCONTRADO se não achar o id
            tupla = hash_table.get(id)
            lista_de_tuplas[i] = (tupla[0], tupla[1], tupla[2])

        end = time()

        # salva num arquivo o tempo de consulta em milisegundos
        with open(f'experimento{tamanho}.txt', 'a') as file:
            file.write(f'Parte 2: ESTATISTICAS DA CONSULTA\n'
                       f'TEMPO PARA REALIZACAO DE TODAS CONSULTAS: {end - start:.5f} milisegundos\n')
            for tupla in lista_de_tuplas:
                file.write(f'{tupla}\n')


def main():

    tamanhos = [997, 1999, 3989, 7993]
    for tamanho in tamanhos:
        hash_table = cria_tabela(tamanho)
        estatisticas_consultas(hash_table, tamanho)

    # hash_table.remove('(id de alguém)') ## testar
    # resize testar


if __name__ == '__main__':
    main()
