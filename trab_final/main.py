from src.hash_table import HashTable
from src.fifa_database import FIFA_Database
from src.interface import Application, cria_interface

from time import time

# Constantes
ID = '130642'  # id do usuário com mais avaliações
TAMANHO_TABELA = 7993

def main():
    fifa_db = FIFA_Database()

    start = time()
    fifa_db.get_players_info()
    fifa_db.get_minirating_info("data/minirating.csv")
    fifa_db._update_global_ratings()  # vamos ver se isso aqui aumenta significativamente quando usarmos o minirating de 24M
    fifa_db.get_tags_info()
    end = time()

    print(
        f'Tempo de construção das estruturas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos\n')


    # fifa_db.tags_HT.cons_stats()

    # Salvando os tabelas
    # with open('../output/players_ht.txt', 'w') as file:
    # file.write(str(fifa_db.players_HT))

    # with open('../output/users_ht.txt', 'w') as file:
    # file.write(str(fifa_db.users_HT))

    with open('output/tags_ht.txt', 'w', encoding='utf-8') as file:
        file.write(str(fifa_db.tags_HT))

    master = cria_interface()
    app = Application(master, fifa_db)
    app.mainloop()

main()
