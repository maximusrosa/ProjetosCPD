from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

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

    def funcao(self):
        # Apaga os dados da tabela
        self.my_tree.delete(*self.my_tree.get_children())
        # Cria elementos pra colocar nas linhas
        for i in range(100):
            self.my_tree.insert(parent='', index='end', iid={i}, text="Parent", values=("Banana", "2", "30", "3123", f"{i}"))

root = tk.Tk()
app = MyApplication(root)
root.mainloop()