import csv
from time import time
from collections import namedtuple

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Constantes
ID = '130642' # id do usuário com mais avaliações
TAMANHO_TABELA = 7993

Avaliacao = namedtuple('Avaliacao', ['player_id', 'nota'])


class Jogador:
    def __init__(self, id, nome_curto, nome, posicoes, nacionalidade, clube, liga):
        self.id = id
        self.nome_curto = nome_curto
        self.nome = nome
        self.posicoes = posicoes
        self.nacionalidade = nacionalidade
        self.clube = clube
        self.liga = liga

        self.soma_notas = self.num_avaliacoes = self.media_global = 0

    def __str__(self):
        return f'({self.id}, {self.nome_curto}, {self.nome}, {self.posicoes}, {self.nacionalidade}, {self.clube}, {self.liga}, {self.media_global:.6f})'


class Usuario:
    def __init__(self, id):
        self.id = id
        self.avaliacoes = []

    def __str__(self):
        return f'({self.id}, {self.avaliacoes})'

    # temos que substituir o ".sort" por um dos algoritmos dos labs
    def get_top_rated_players(self, players_ht):
        # Create a list of tuples containing player_id, user_rating, global_average, and count of ratings
        top_rated_players = [(avaliacao.player_id, avaliacao.nota, players_ht.get(avaliacao.player_id).media_global)
                             for avaliacao in self.avaliacoes]

        # Sort the list in descending order by user_rating and then by global_average
        top_rated_players.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Return the top 20 players
        return str(top_rated_players[:20])

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):
        
        button=tk.Button(self.master, text="Print Oi", command=print_oi)
        button.place(x=50, y=250)

        button1 = tk.Button(self.master, text="Confirmar", command=confirm)
        button1.place(x=150, y=250)

        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('country', 'capital', 'currency', 'teste', 'mais colunas', 'vamo', 'irra')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        
        # Barra de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        self.tree['yscroll'] = ysb.set
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:
        self.data = [
            ("Argentina",      "Buenos Aires",     "ARS", "teste", "yei", "mais uma"),
            ("Australia",      "Canberra",         "AUD", "hummmmmmmmmmmmmmmmmmmmmmmmmmmm"),
            ("Brazil",         "Brazilia",         "BRL"),
            ("Canada",         "Ottawa",           "CAD"),
            ("China",          "Beijing",          "CNY"),
            ("France",         "Paris",            "EUR"),
            ("Germany",        "Berlin",           "EUR"),
            ("India",          "New Delhi",        "INR"),
            ("Italy",          "Rome",             "EUR"),
            ("Japan",          "Tokyo",            "JPY"),
            ("Mexico",         "Mexico City",      "MXN"),
            ("Russia",         "Moscow",           "RUB"),
            ("South Africa",   "Pretoria",         "ZAR"),
            ("United Kingdom", "London",           "GBP"),
            ("United States",  "Washington, D.C.", "USD"),
        ]

        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)

def print_oi():
    print("Oi")

def confirm():
    response = messagebox.askyesno("Confirmação", "Você tem certeza?")
    if response:
        print("Você clicou em Sim")
    else:
        print("Você clicou em Não")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __str__(self):
        output = ""

        for i, lista in enumerate(self.table):
            output += f"{i}: "

            if lista:
                output += ", ".join([str(object) for object in lista])

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

    def _resize(self):
        self.size *= 2  # Dobra o tamanho da tabela hash
        new_table = [[] for _ in range(self.size)]

        for bucket in self.table:
            for _ in bucket:
                index = self._hash(_.id[0])
                new_table[index].append(_)

        self.table = new_table
        del new_table

    def insert(self, object: Jogador | Usuario):
        index = self._hash(object.id)
        self.table[index].append(object)

        # Se a taxa de ocupação dessa lista encadeada é maior que 20% do tamanho da tabela hash
        if len(self.table[index]) / self.size > 0.2:
            self._resize()  # Redimensiona a tabela hash

    def get(self, id):
        index = self._hash(id)

        for object in self.table[index]:
            if object.id == id:
                return object

        raise ValueError(f'{id} NAO ENCONTRADO')

    def update_user(self, user_id, rating: Avaliacao):
        index = self._hash(user_id)

        for usuario in self.table[index]:
            if usuario.id == user_id:
                usuario.avaliacoes.append(rating)
                return

        # Se não achar o usuário, insere ele na tabela hash de usuários
        novo_usuario = Usuario(user_id)
        novo_usuario.avaliacoes.append(rating)
        self.insert(novo_usuario)

    def update_global_ratings(self):
        start = time()

        for lista in self.table:
            for jogador in lista:
                if jogador.num_avaliacoes != 0:
                    jogador.media_global = jogador.soma_notas / jogador.num_avaliacoes

        end = time()
        print(f'Tempo para atualizar as médias globais: {(end - start) * 1000:.4f} milisegundos')

    def get_top_players_by_position(self, position, n):
        top_players = [(jogador.id, jogador.media_global)
                       for lista in self.table for jogador in lista
                       if position in jogador.posicoes and jogador.num_avaliacoes >= 0]

        top_players.sort(key=lambda x: x[1], reverse=True)

        return top_players[:n]

    def get_players_info(self):

        # Lista todos os arquivos e diretórios no diretório atual
        for nome in os.listdir('.'):
            # Se for um diretório, imprime o nome
            if os.path.isdir(nome):
                print(nome)
                
        with open('../data/players.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            for row in reader:
                self.insert(Jogador(id=row[0], nome_curto=row[1], nome=row[2], posicoes=row[3],
                                    nacionalidade=row[4], clube=row[5], liga=row[6]))

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

    def remove(self, id):  # N vai precisar pro trabalho, porém dá pra usar na interface pra tirar alguém da tabela
        index = self._hash(id)

        for i, jogador in enumerate(self.table[index]):
            if jogador.id == id:
                self.table[index].pop(i)
                print("Jogador removido")
                return

        print("Jogador não encontrado")

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

    # -------------------------------------------------------------------------------- #

def get_minirating_info(players_ht, users_ht):
    with open('../data/minirating.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            users_ht.update_user(row[0], Avaliacao(player_id=row[1], nota=row[2]))  # A coluna 0 é o id do usuário

            index = players_ht._hash(row[1])  # Índice na tabela do jogador do id atual

            for jogador in players_ht.table[index]:
                if jogador.id == row[1]:
                    jogador.soma_notas += float(row[2])
                    jogador.num_avaliacoes += 1

def find_user_with_most_reviews(users_ht):
    max_reviews = 0
    user_with_most_reviews = None

    # Percorre todas as listas na tabela hash
    for user_list in users_ht.table:
        # Percorre todos os usuários em cada lista
        for user in user_list:
            # Se o usuário atual tem mais avaliações do que o máximo atual
            if len(user.avaliacoes) > max_reviews:
                # Atualiza o máximo e o usuário com mais avaliações
                max_reviews = len(user.avaliacoes)
                user_with_most_reviews = user

    return user_with_most_reviews


def main():
    players_ht = HashTable(TAMANHO_TABELA)
    users_ht = HashTable(TAMANHO_TABELA)

    start = time()
    players_ht.get_players_info()
    get_minirating_info(players_ht, users_ht)
    players_ht.update_global_ratings()
    end = time()

    print(f'Tempo de construção das tabelas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')

    # Ex: Procurando o Messi
    #print(str(players_ht.get("158023")))

    # pras pesquisas, ainda temos que decidir quais algoritmos de ordenação usar

    # Pesquisa 2: jogadores revisados por usuários
    print(users_ht.get(ID).get_top_rated_players(players_ht))

    # Pesquisa 3: melhores jogadores de uma determinada posição
    print(players_ht.get_top_players_by_position("ST", 10))


    # Salvando os tabelas
    with open('../output/players_ht.txt', 'w') as file:
        file.write(str(players_ht))

    with open('../output/users_ht.txt', 'w') as file:
        file.write(str(users_ht))




    master = tk.Tk()
    master.title("Trabalho Final CPD - Thiago Vito e Maximus Borges")  # Muda o nome da janela
    screen_width = master.winfo_screenwidth() # Largura da tela
    master.geometry(f"{screen_width - 50}x310") # Tamanho da janela
    #master.configure(bg='white')  # Define a cor de fundo da janela para branco

    app = Application(master)
    app.mainloop()

if __name__ == '__main__':
    main()