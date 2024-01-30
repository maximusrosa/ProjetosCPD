from src.fifa_database import FIFA_Database
from src.interface import MyApplication

from time import time

import tkinter as tk


def main():
    # Pré-processamento
    start = time()

    fifa_db = FIFA_Database()

    fifa_db.get_players_info()

    fifa_db.get_tags_info()

    fifa_db.get_rating_info('data/rating.csv')

    end = time()

    print(
        f'\nTempo de construção das estruturas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')

    # Interface gráfica
    root = tk.Tk()
    MyApplication(root, fifa_db)
    root.mainloop()

main()
