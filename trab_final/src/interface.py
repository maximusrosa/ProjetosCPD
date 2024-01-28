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


class MyApplication:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x520')

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("yu gothic vi", 10, "bold"))

        self.scrollbarx = Scrollbar(root, orient=tk.HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=tk.VERTICAL)

        self.my_tree = ttk.Treeview(root)
        self.my_tree.place(relx=0.01, rely=0.128, width=1292, height=410)
        self.my_tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.my_tree.configure(selectmode="extended")

        self.scrollbary.configure(command=self.my_tree.yview)
        self.scrollbarx.configure(command=self.my_tree.xview)

        self.scrollbary.place(relx=0.934, rely=0.128, width=22, height=432)
        self.scrollbarx.place(relx=0.002, rely=0.922, width=1302, height=22)

        self.my_tree.configure(
            columns=(
                "sofifa_id", 
                "short_name", 
                "long_name", 
                "player_positions", 
                "nationality", 
                "club_name", 
                "league_name", 
                "global_rating", 
                "count"
            ),
            show='headings'  # Oculta a coluna extra
        )

        self.set_widgets()
        self.mostrar_elementos()

    def set_widgets(self):
        # Cria as colunas
        self.my_tree.heading("sofifa_id", text="sofifa_id")
        self.my_tree.heading("short_name", text="short_name")
        self.my_tree.heading("long_name", text="long_name")
        self.my_tree.heading("player_positions", text="player_positions")
        self.my_tree.heading("nationality", text="nationality")
        self.my_tree.heading("club_name", text="club_name")
        self.my_tree.heading("league_name", text="league_name")
        self.my_tree.heading("global_rating", text="global_rating")
        self.my_tree.heading("count", text="count")

        # Cria um botão que imprime "Oi" quando clicado
        self.button = Button(self.root, text="Print Oi", command=self.funcao)
        self.button.place(relx=0.01, rely=0.04, width=100, height=30)  # Posiciona o botão na janela

        # Cria uma caixa de texto pra digitar algo e um botão que imprime o que foi digitado
        self.entry = Entry(self.root)
        self.entry.place(relx=0.2, rely=0.04, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button2 = Button(self.root, text="Print", command=lambda: print(self.entry.get()))
        self.button2.place(relx=0.12, rely=0.01, width=100, height=30)  # Posiciona o botão na janela

    def mostrar_elementos(self):
        # Cria elementos pra colocar nas linhas
        for i in range(100):
            if i % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid={i}, text="Parent", values=("John", "1", "1000", "123456789", f"{i}@gmail.com", "IT", "Manager", "Address"), tags='evenrow')
            else:
                self.my_tree.insert(parent='', index='end', iid={i}, text="Parent", values=("John", "1", "1000", "123456789", f"{i}@gmail.com", "IT", "Manager", "Address"))

        # Configura a cor de fundo das linhas pares
        self.my_tree.tag_configure('evenrow', background='#f2f2f2')

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



    def _limpa_tabela(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


