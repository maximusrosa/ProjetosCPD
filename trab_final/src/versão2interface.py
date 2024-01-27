import tkinter as tk
from tkinter import ttk

import random
import string

def atualizar():
    # Atualiza os nomes das colunas
    for i, col in enumerate(tree['columns']):
        tree.heading(col, text=f'Nova Coluna {i+1}')

    # Limpa o Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Adiciona novos itens ao Treeview
    for i in range(1000):
        # Gera uma letra aleatória do alfabeto
        letra = random.choice(string.ascii_letters)
        # Aplica o estilo 'linha_par' às linhas pares
        tree.insert('', 'end', values=(f'Item {letra} Nova Coluna 1', f'Item {letra} Nova Coluna 2', f'Item {letra} Nova Coluna 3', f'Item {letra} Nova Coluna 4', f'Item {letra} Nova Coluna 5'), tags=('linha_par' if i % 2 == 0 else ''))

def atualizar_com_texto(entry):
    # Pega o texto digitado pelo usuário
    texto = entry.get()

    # Limpa o Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Adiciona novos itens ao Treeview com o texto digitado
    for i in range(1000):
        # Aplica o estilo 'linha_par' às linhas pares
        tree.insert('', 'end', values=(f'Item {texto} Coluna 1', f'Item {texto} Coluna 2', f'Item {texto} Coluna 3', f'Item {texto} Coluna 4', f'Item {texto} Coluna 5'), tags=('linha_par' if i % 2 == 0 else ''))

root = tk.Tk()

# Cria um frame
frame = tk.Frame(root)
frame.grid()

# Cria um widget Canvas e adiciona ao frame
canvas = tk.Canvas(frame, highlightthickness=0)
canvas.grid(row=0, column=0)

# Cria um widget Treeview com mais colunas e adiciona ao Canvas
tree = ttk.Treeview(canvas, columns=('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5'), show='headings')

# Configura as colunas
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=200)  # Aumenta a largura das colunas

# Define um estilo para as linhas pares
tree.tag_configure('linha_par', background='#f2f2f2')

# Adiciona mais itens ao Treeview
for i in range(1000):
    # Aplica o estilo 'linha_par' às linhas pares
    tree.insert('', 'end', values=(f'Item {i} Coluna 1', f'Item {i} Coluna 2', f'Item {i} Coluna 3', f'Item {i} Coluna 4', f'Item {i} Coluna 5'), tags=('linha_par' if i % 2 == 0 else ''))

# Adiciona o Treeview ao Canvas
canvas.create_window((0,0), window=tree, anchor='nw')

# Cria uma barra de rolagem horizontal e adiciona ao frame
h_scrollbar = tk.Scrollbar(frame, orient='horizontal', command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky='ew')

# Cria uma barra de rolagem vertical e adiciona ao frame
v_scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky='ns')

# Configura o widget Canvas para usar as barras de rolagem
canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

def print_oi():
    print("Oi")

# Cria um botão e adiciona ao frame
botao = tk.Button(frame, text="Clique aqui", command=print_oi)
botao.grid(row=2, column=0, sticky='ew')

# Cria um botão e adiciona ao frame
botao = tk.Button(frame, text="Atualizar", command=atualizar)
botao.grid(row=3, column=0, sticky='ew')

# Cria um campo de entrada e adiciona ao frame
entry = tk.Entry(frame)
entry.grid(row=4, column=0, sticky='ew')

# Cria um botão e adiciona ao frame
botao = tk.Button(frame, text="Atualizar com texto", command=lambda:atualizar_com_texto(entry))
botao.grid(row=5, column=0, sticky='ew')

# Configura o evento de rolagem do Canvas para atualizar a região de rolagem
def on_configure(event, canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas.bind('<Configure>', lambda event: on_configure(event, canvas))

root.mainloop()