from src.fifa_database import FIFA_Database

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import csv

class MyApplication:
    def __init__(self, root, base_de_dados):
        self.root = root
        self.root.geometry('1400x620')
        self.root.title("Trabalho Final CPD - Thiago Vito e Maximus Borges")
        self.base_de_dados = base_de_dados

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("yu gothic vi", 10, "bold"))

        self.scrollbarx = Scrollbar(root, orient=tk.HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=tk.VERTICAL)

        self.my_tree = ttk.Treeview(root)
        self.my_tree.place(relx=0.01, rely=0.2, width=1292, height=410)
        self.my_tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.my_tree.configure(selectmode="extended")

        self.scrollbary.configure(command=self.my_tree.yview)
        self.scrollbarx.configure(command=self.my_tree.xview)

        self.scrollbary.place(relx=0.934, rely=0.2, width=22, height=432)
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
                "count",
                "rating"
            ),
            show='headings'  # Oculta a coluna extra
        )
    
        # Configura a cor de fundo das linhas pares
        self.my_tree.tag_configure('evenrow', background='#f2f2f2')

        self.set_widgets()
        self.mostrar_players()

    def mostrar_players(self):
        with open('data/players.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            row = next(reader)
            self.limpa_tabela()
            for i, row in enumerate(reader):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], '', ''), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], '', ''))


    def set_widgets(self):
        # Cria as colunas da tabela
        colunas = ["sofifa_id", "short_name", "long_name", "player_positions", "nationality", "club_name", "league_name", "global_rating", "count", "rating"]
        for coluna in colunas:
            self.my_tree.heading(coluna, text=coluna)

        # Cria um botão que mostra os jogadores
        self.button = Button(self.root, text="Mostrar jogadores", command=self.mostrar_players)
        self.button.place(relx=0.01, rely=0.04, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry = Entry(self.root)
        self.entry.place(relx=0.245, rely=0.04, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button = Button(self.root, text="Procura por prefixo", command=lambda: self.procura_por_prefixo(self.entry.get()))
        self.button.place(relx=0.145, rely=0.04, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry2 = Entry(self.root)
        self.entry2.place(relx=0.445, rely=0.04, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button2 = Button(self.root, text="Procura por usuário", command=lambda: self.procura_por_usuario(self.entry2.get()))
        self.button2.place(relx=0.345, rely=0.04, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry3 = Entry(self.root)
        self.entry3.place(relx=0.645, rely=0.04, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.entry4 = Entry(self.root)
        self.entry4.place(relx=0.705, rely=0.04, width=25, height=30)  # Posiciona a caixa de texto na janela
        self.button3 = Button(self.root, text="Procura por posição", command=lambda: self.procura_por_posicao(self.entry4.get(), self.entry3.get()))
        self.button3.place(relx=0.545, rely=0.04, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry5 = Entry(self.root)
        self.entry5.place(relx=0.14, rely=0.12, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button5 = Button(self.root, text="Procura por tags", command=lambda: self.procura_por_tags(self.entry5.get()))
        self.button5.place(relx=0.04, rely=0.12, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry6 = Entry(self.root)
        self.entry6.place(relx=0.34, rely=0.12, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button6 = Button(self.root, text="Procura por clube", command=lambda: self.procura_por_clube(self.entry6.get()))
        self.button6.place(relx=0.24, rely=0.12, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry7 = Entry(self.root)
        self.entry7.place(relx=0.54, rely=0.12, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button7 = Button(self.root, text="Procura por país", command=lambda: self.procura_por_nacionalidade(self.entry7.get()))
        self.button7.place(relx=0.44, rely=0.12, width=130, height=30)  # Posiciona o botão na janela

        # Cria uma entrada de texto
        self.entry8 = Entry(self.root)
        self.entry8.place(relx=0.74, rely=0.12, width=100, height=30)  # Posiciona a caixa de texto na janela
        self.button8 = Button(self.root, text="Procura por liga", command=lambda: self.procura_por_liga(self.entry8.get()))
        self.button8.place(relx=0.64, rely=0.12, width=130, height=30)  # Posiciona o botão na janela


    def procura_por_prefixo(self, prefixo):

        if not isinstance(prefixo, str) or prefixo == '':
            messagebox.showerror("Erro", "Digite um prefixo válido")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pelo prefixo {prefixo}?")
        if response:

            self.limpa_tabela()
            for i, player in enumerate(self.base_de_dados.top_by_prefix(prefixo)):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))

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
                lista = self.base_de_dados.top_by_user(usuario)
            except Exception:
                messagebox.showerror("Erro", "Usuário não encontrado")
                return

            self.limpa_tabela()
            for i, (player, rating) in enumerate(lista):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes, rating), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes, rating))

        else:
            return

    def procura_por_posicao(self, n, posicao):
        
        if not isinstance(posicao, str) or posicao == '':
            messagebox.showerror("Erro", "Digite uma posição válida")
            return
        
        try:
            int(n) # Se conseguir transformar pra inteiro a string é um id válido
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pela posição {posicao}?")
        if response:

            self.limpa_tabela()
            for i, player in enumerate(self.base_de_dados.top_by_position(int(n), posicao)):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))

        else:
            return

    def procura_por_tags(self, tags):

        if not isinstance(tags, str) or tags == '':
            messagebox.showerror("Erro", "Digite um prefixo válido")
            return

        response = messagebox.askyesno("Confirmação", f"Buscar pela(s) tag(s) {tags}?")
        if response:

            self.limpa_tabela()
            for i, player in enumerate(self.base_de_dados.top_by_tags(tags.split(", "))):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))
        else:
            return
        
    def procura_por_clube(self, clube):
            
            if not isinstance(clube, str) or clube == '':
                messagebox.showerror("Erro", "Digite um clube válido")
                return
    
            response = messagebox.askyesno("Confirmação", f"Buscar pelo clube {clube}?")
            if response:
                self.limpa_tabela()
                for i, player in enumerate(self.base_de_dados.top_by_club(clube)):
                    if i % 2 == 0:
                        self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                    else:
                        self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))
            else:
                return
            
    def procura_por_nacionalidade(self, nacionalidade):
        
        if not isinstance(nacionalidade, str) or nacionalidade == '':
            messagebox.showerror("Erro", "Digite uma nacionalidade válida")
            return
        
        response = messagebox.askyesno("Confirmação", f"Buscar pela nacionalidade {nacionalidade}?")
        if response:
            self.limpa_tabela()
            for i, player in enumerate(self.base_de_dados.top_by_nationality(nacionalidade)):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))

    def procura_por_liga(self, liga):
                
        if not isinstance(liga, str) or liga == '':
            messagebox.showerror("Erro", "Digite uma nacionalidade válida")
            return
        
        response = messagebox.askyesno("Confirmação", f"Buscar pela liga {liga}?")
        if response:
            self.limpa_tabela()
            for i, player in enumerate(self.base_de_dados.top_by_league(liga)):
                if i % 2 == 0:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes), tags=('evenrow',))
                else:
                    self.my_tree.insert('', 'end', values=(player.id, player.nome_curto, player.nome_longo, player.posicoes, player.nacionalidade, player.clube, player.liga, player.media_global, player.num_avaliacoes))



    def limpa_tabela(self):
        self.my_tree.delete(*self.my_tree.get_children())



