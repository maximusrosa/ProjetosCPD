from src.fifa_database import FIFA_Database
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import csv, time

def cria_interface():

    master = tk.Tk()  # Cria a interface

    # Muda o nome da janela
    master.title("Trabalho Final CPD - Thiago Vito e Maximus Borges")
    screen_width = master.winfo_screenwidth()  # Largura da tela
    master.geometry(f"{screen_width - 100}x310")  # Tamanho da janela
    # master.configure(bg='white')  # Define a cor de fundo da janela para branco

    master.dataCols = ('', '', '', '', '', '', '')
    master.tree = ttk.Treeview(columns=master.dataCols, show='headings')
    master.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

    # Barra de rolagem
    ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=master.tree.yview)
    master.tree.configure(yscrollcommand=ysb.set)
    ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

    return master


class Application(tk.Frame):

    def __init__(self, master=None, base_de_dados_fifa=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()
        self.data = []
        self.base_de_dados = base_de_dados_fifa
        self.mostrar_players()

    def mostrar_players(self):
        with open('data/players.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            row = next(reader)

            # Inicia o Treeview com as seguintes colunas:
            self.dataCols = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
            self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            # Barra de rolagem
            xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
            ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set)
            xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
            ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data.clear()
            for row in reader:
                self.data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def procura_por_prefixo(self, prefixo):

        if not isinstance(prefixo, str) or prefixo == '':
            messagebox.showerror("Erro", "Digite um prefixo válido")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pelo prefixo {prefixo}?")
        if response:

            # Inicia o Treeview com as seguintes colunas:
            self.dataCols = ("sofifa_id", "short_name", "long_name", "player_positions", "global_rating", "count")
            self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
            self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            # Barra de rolagem
            ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=ysb.set)
            ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data.clear()
            for player in self.base_de_dados.top_by_prefix(prefixo):
                self.data.append((player.id, player.nome_curto, player.nome, player.posicoes, player.media_global, player.num_avaliacoes))

            for item in self.data:
                self.tree.insert('', 'end', values=item)

        else:
            return
        
    def procura_por_usuario(self, usuario):

        try:
            int(usuario) # Se conseguir transformar pra inteiro a string é um id válido
        except ValueError:
            messagebox.showerror("Erro", "Digite um usuário válido")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pelo usuário {usuario}?")
        if response:
            try:
                print(self.base_de_dados.top_by_user(usuario))
                avaliacoes = self.base_de_dados.top_by_user(usuario)
            except Exception:
                messagebox.showerror("Erro", "Usuário não encontrado")
                return

            # Inicia o Treeview com as seguintes colunas:
            self.dataCols = ("sofifa_id", "short_name", "long_name", "global_rating", "count", "rating")
            self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
            self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            # Barra de rolagem
            ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=ysb.set)
            ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data.clear()
            for avaliacao in avaliacoes:
                player = self.base_de_dados.players_HT.get(avaliacao[0])
                self.data.append((avaliacao[0], player.nome_curto, player.nome, player.media_global, player.num_avaliacoes, avaliacao[1]))

            for item in self.data:
                self.tree.insert('', 'end', values=item)

        else:
            return

    def procura_por_posicao(self, posicao):
        
        if not isinstance(posicao, str) or posicao == '':
            messagebox.showerror("Erro", "Digite uma posição válida")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pela posição {posicao}?")
        if response:

            # Inicia o Treeview com as seguintes colunas:
            self.dataCols = ("sofifa_id", "short_name", "long_name", "player_positions", "nationality", "club_name", "league_name", "global_rating", "count")
            self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
            self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            # Barra de rolagem
            xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
            ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set)
            xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
            ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data.clear()
            for player in self.base_de_dados.top_by_position(10, posicao):
                self.data.append((player[0], player[1], player[2], player[3], player[4], player[5], player[6], player[7], player[8]))

            for item in self.data:
                self.tree.insert('', 'end', values=item)
            
        else:
            return

    def set_widgets(self):
        
        funcao = tk.Button(self.master, text="Mostrar jogadores", command=self.mostrar_players)
        funcao.place(x=60, y=250)

        # pesquisa1 prefixo dos jogadores ordenados por rating
        # pesquisa2 por id do usuario que mostra ordenado por rating e depois global_rating
        # pesquisa3 top10 jogadores de uma posição tipo 'ST' ordenados por RATING
        # pesquisa4 pesquisa por jogador.posições e jogador.nacionalidade ordenados por rating

        # Entrada 1
        prefixo = tk.Entry(width=34)  # Digita o nome do jogador aqui
        prefixo.place(x=260, y=240)
        prefixo.focus()  # Deixa o cursor na entrada
        add_button = tk.Button(text="Busca por prefixo", width=33, command=lambda: self.procura_por_prefixo(prefixo.get()))
        add_button.place(x=260, y=260)

        # Entrada 2
        usuario = tk.Entry(width=34)  # Digita o id do usuário aqui
        usuario.place(x=600, y=240)
        usuario.focus()  # Deixa o cursor na entrada
        add_button = tk.Button(text="Busca por usuário", width=33, command=lambda: self.procura_por_usuario(usuario.get()))
        add_button.place(x=600, y=260)

        # Entrada 3
        posicao = tk.Entry(width=34)  # Digita o id do usuário aqui
        posicao.place(x=940, y=240)
        posicao.focus()  # Deixa o cursor na entrada
        add_button = tk.Button(text="Busca por posição", width=33, command=lambda: self.procura_por_posicao(posicao.get()))
        add_button.place(x=940, y=260)


    def _limpa_tabela(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


