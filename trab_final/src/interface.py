import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):

        with open('data/players.csv', 'r') as file:
            reader = csv.reader(file)
            row = next(reader)

            button=tk.Button(self.master, text="Print Oi", command=print_oi, height=2, width=10)
            button.place(x=50, y=250)

            button1 = tk.Button(self.master, text="Confirmar", command=confirm)
            button1.place(x=150, y=250)

            # Inicia o Treeview com as seguintes colunas:
            self.dataCols = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
            self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            # Barra de rolagem
            ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
            self.tree['yscroll'] = ysb.set
            ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

            # Define o textos do cabeçalho (nome em maiúsculas)
            for c in self.dataCols:
                self.tree.heading(c, text=c.title())

            self.data = []
            for row in reader:
                self.data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

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