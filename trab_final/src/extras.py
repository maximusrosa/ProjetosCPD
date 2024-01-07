# ------------------------------------ Extras ------------------------------------ #

# Vamo mostrar essas informações na interface pra ganhar uns pontinho extra
def _average_list_size(self):
    soma = 0
    contador = 0

    for lista in self.table:
        if lista:  # se a lista não estiver vazia
            soma += len(lista)
            contador += 1

    media = soma / contador if contador != 0 else 0

    return media

def cons_stats(self):
    start = time()
    self.get_players_info()
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

    with open(f'experimento.txt', 'w') as file:
        file.write(f'Parte 1: ESTATISTICAS DA TABELA HASH\n'
                   f'Tempo de construcao da tabela: {end - start:.5f} segundos ou {(end - start) * 1000:.5f} milisegundos\n'
                   f'Taxa de ocupacao: {(posicoes_ocupadas / self.size) * 100:.2f}%\n'
                   f'Tamanho maximo de lista: {tamanho_max:.0f} elementos\n'
                   f'Tamanho medio de lista: {media:.1f} elementos\n\n')

# se for usar, tem que mudar o retorno da "get"
def queries_stats(self):  # acho que não precisa disso pro trabalho
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

    with open(f'experimento.txt', 'a') as file:
        file.write(f'Parte 2: ESTATISTICAS DA CONSULTA\n'
                   f'TEMPO PARA REALIZACAO DE TODAS CONSULTAS: {end - start:.5f} milisegundos\n')
        for info_consulta in consultas:
            file.write(f'{info_consulta}\n')

def remove(self, id):  # N vai precisar pro trabalho, porém dá pra usar na interface pra tirar alguém da tabela
    index = self._hash(id)

    for i, jogador in enumerate(self.table[index]):
        if jogador.id == id:
            self.table[index].pop(i)
            print("Jogador removido")
            return

    print("Jogador não encontrado")

# -------------------------------------------------------------------------------- #