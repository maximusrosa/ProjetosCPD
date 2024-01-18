import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import csv

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

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def comando(self):
        response = messagebox.askyesno("Confirmação", "Isso irá te mostrar os dados do arquivo {players.csv}. Você tem certeza?")
        if response:
            with open('data/players.csv', 'r') as file:
                reader = csv.reader(file)
                row = next(reader)

                # Inicia o Treeview com as seguintes colunas:
                self.dataCols = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
                self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

                # Barra de rolagem
                ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
                self.tree.configure(yscrollcommand=ysb.set)
                ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data = []
            for row in reader:
                self.data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                for item in self.data:
                    self.tree.insert('', 'end', values=item)
        else:
            return

    def set_widgets(self):
        
        funcao = tk.Button(self.master, text="Função", command=lambda: self.comando())
        funcao.place(x=150, y=250)

        # Labels
        variavel_label = tk.Label(text="Procura por ID:")
        variavel_label.grid(row=3, column=0)

        # Entries
        variavel = tk.Entry(width=35)  # Digita o nome do jogador aqui
        variavel.grid(row=4, column=0, columnspan=2)
        variavel.focus()  # Deixa o cursor na entrada
        add_button = tk.Button(text="Aperte esse botão", width=36, command=lambda: self.faz_algo(variavel))
        add_button.grid(row=5, column=0, columnspan=2)

    def limpa_tabela(self):
        response = messagebox.askyesno("Confirmação", "Isso irá limpar a tabela. Você tem certeza?")
        if response:  # Se o usuário confirmar, limpa a tabela
            for i in self.tree.get_children():
                self.tree.delete(i)

    def faz_algo(self, variavel):
        response = messagebox.askyesno("Confirmação", "Isso irá fazer algo. Você tem certeza?")
        if response:  # Se o usuário confirmar, faz algo
            print(variavel.get())
