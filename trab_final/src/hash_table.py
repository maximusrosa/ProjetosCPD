from collections import namedtuple
import csv
from time import time


class Jogador:
    def __init__(self, id, nome_curto, nome, posicoes, nacionalidade, clube, liga, soma_notas, num_avaliacoes, media_global):
        self.id = id
        self.nome_curto = nome_curto
        self.nome = nome
        self.posicoes = posicoes
        self.nacionalidade = nacionalidade
        self.clube = clube
        self.liga = liga
        self.soma_notas = soma_notas
        self.num_avaliacoes = num_avaliacoes
        self.media_global = media_global

    def __str__(self):
        return f'({self.id}, {self.nome_curto}, {self.nome}, {self.posicoes}, {self.nacionalidade}, {self.clube}, {self.liga}, {self.soma_notas}, {self.num_avaliacoes}, {self.media_global:.6f})'


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __str__(self):
        output = ""

        for i, lista_jogadores in enumerate(self.table):
            output += f"{i}: "

            if lista_jogadores:
                output += ", ".join(
                    [
                        f'({jogador.id}, {jogador.nome_curto}, {jogador.nome}, {jogador.posicoes}, {jogador.nacionalidade}, {jogador.clube}, {jogador.liga}, {jogador.soma_notas}, {jogador.num_avaliacoes}, {jogador.media_global})'
                        for jogador in lista_jogadores])

            output += "\n"

        return output

    def _hash(self, id: str) -> int:
        # lista de números primos com o 1
        numeros = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        resultado = 1

        for i, digito in enumerate(str(id)):
            # Ex: id = 357741 -> 1^3 + 2^5 + 3^7 + 5^7 + 7^4 + 11^1
            resultado += numeros[i] ** int(digito)

        return resultado % self.size

    # Se a taxa de ocupação de uma das listas encadeadas é maior que 70%
    # if len(self.table[hash_index]) / self.size > 0.7:
    #   self._resize()  # Redimensiona a tabela hash
    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]

        for bucket in self.table:
            for jogador in bucket:
                hash_index = self._hash(jogador.id[0])
                new_table[hash_index].append(jogador)

        self.table = new_table

    def insert(self, Jogador):
        hash_index = self._hash(Jogador.id)

        self.table[hash_index].append(Jogador)

    def get(self, id):
        cmps = 0
        hash_index = self._hash(id)

        for jogador in self.table[hash_index]:
            cmps += 1
            if jogador.id == id:
                # print("Jogador encontrado.")
                return f"{id}", f"{jogador.nome}", cmps

        # print("Jogador não encontrado.")
        return f"{id}", "NAO ENCONTRADO", cmps

    def remove(self, id):
        hash_index = self._hash(id)

        for i, jogador in enumerate(self.table[hash_index]):
            if jogador.id == id:
                self.table[hash_index].pop(i)
                print("Jogador removido")
                return

        print("Jogador não encontrado")

    def _average_list_size(self):
        soma = 0
        contador = 0

        for lista in self.table:
            if lista:  # se a lista não estiver vazia
                soma += len(lista)
                contador += 1

        media = soma / contador if contador != 0 else 0

        return media

    def fill(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            for row in reader:
                id = row[0]
                nome_curto = row[1]
                nome = row[2]
                posicoes = row[3]
                nacionalidade = row[4]
                clube = row[5]
                liga = row[6]
                self.insert(Jogador(id, nome_curto, nome, posicoes,
                                    nacionalidade, clube, liga, 0, 0, 0))

    def cons_stats(self):
        with open('../data/players.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            start = time()

            for row in reader:
                id = row[0]
                nome_curto = row[1]
                nome = row[2]
                posicoes = row[3]
                nacionalidade = row[4]
                clube = row[5]
                liga = row[6]

                # insere na tabela todos os valores acima
                self.insert(Jogador(id, nome_curto, nome, posicoes,
                            nacionalidade, clube, liga, 0, 0, 0))

            end = time()

            # calcula a média do tamanho das listas não vazias
            media = self._average_list_size()

            # maior tamanho de lista
            tamanho_max = max([len(lista) for lista in self.table])

            # conta o número de posições do "array" com listas não vazias
            posicoes_ocupadas = 0

            for lista in self.table:
                if lista:
                    posicoes_ocupadas += 1

        with open(f'experimento{self.size}.txt', 'w') as file:
            file.write(f'Parte 1: ESTATISTICAS DA TABELA HASH\n'
                       f'Tempo de construcao da tabela: {end - start:.5f} segundos ou {(end - start) * 1000:.5f} milisegundos\n'
                       f'Taxa de ocupacao: {(posicoes_ocupadas / self.size) * 100:.2f}%\n'
                       f'Tamanho maximo de lista: {tamanho_max:.0f} elementos\n'
                       f'Tamanho medio de lista: {media:.1f} elementos\n\n')

    def queries_stats(self):
        with open(f'../data/consultas.csv', 'r') as file:
            reader = list(csv.reader(file))

            consultas = [None] * len(reader)

            start = time()

            for i, row in enumerate(reader):
                id = row[0]

                # retorna uma tupla com o (id, nome, num_comparações) mas nome = NAO ENCONTRADO se não achar o id
                info_consulta = self.get(id)
                consultas[i] = info_consulta

            end = time()

        with open(f'experimento{self.size}.txt', 'a') as file:
            file.write(f'Parte 2: ESTATISTICAS DA CONSULTA\n'
                       f'TEMPO PARA REALIZACAO DE TODAS CONSULTAS: {end - start:.5f} milisegundos\n')
            for info_consulta in consultas:
                file.write(f'{info_consulta}\n')

    def minirating(self):
        with open('../data/minirating.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Acha o index do jogador do id atual
                hash_index = self._hash(row[1])

                # Percorre a lista de jogadores do id atual
                for jogador in self.table[hash_index]:
                    if jogador.id == row[1]:
                        # Quando achar o jogador, atualiza a soma das notas e o número de avaliações
                        jogador.soma_notas += float(row[2])
                        jogador.num_avaliacoes += 1

                # Atualiza a média global de todos os jogadores da tabela hash
                for lista_jogadores in self.table:
                    for jogador in lista_jogadores:
                        if jogador.num_avaliacoes != 0:
                            jogador.media_global = jogador.soma_notas / jogador.num_avaliacoes

    # Procura o Messi na tabela hash e printa suas informações pra verificar a media global do enunciado !
            for jogador in self.table[self._hash("158023")]:
                if jogador.id == "158023":
                    print(jogador, end='\n\n')
                    break


def main():
    tamanho = 7993
    hash_table = HashTable(tamanho)

    start = time()
    hash_table.fill('../data/players.csv')
    end = time()

    print(
        f'Tempo de construção da tabela: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')

    hash_table.minirating()  # Atualiza a tabela hash com a média global

    # Escreve no arquivo a tabela hash com a média global atualizada
    with open('../output/hash_table.txt', 'w') as file:
        file.write(str(hash_table))

    print(hash_table)

    # hash_table.remove('(id de alguém)') ## testar
    # resize testar


if __name__ == '__main__':
    main()
