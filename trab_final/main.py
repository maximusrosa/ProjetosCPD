from src.hash_table import FIFA_Database
from src.interface import Application, cria_interface

from time import time
from collections import namedtuple

# Constantes
ID_USER_MAX = '130642' # id do usuário com mais avaliações
FILENAME = 'data/players.csv'

def main():
    fifa_db = FIFA_Database()

    start = time()
    fifa_db.get_players_info(FILENAME)
    fifa_db.get_minirating_info(FILENAME)
    fifa_db.update_global_ratings()
    end = time()

    print(f'Tempo de construção das tabelas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')


    # Ex: Procurando o Messi
    print(str(fifa_db.players_HT.get("158023")))

    # Pesquisa 2: jogadores revisados por usuários
    print(fifa_db.top_by_user(ID_USER_MAX))

    # Pesquisa 3: melhores jogadores de uma determinada posição
    print(fifa_db.top_by_position("ST", 6))


    # Salvando os tabelas
    #with open('output/players_ht.txt', 'w') as file:
        #file.write(str(players_ht))

    #with open('output/users_ht.txt', 'w') as file:
    #    file.write(str(users_ht))

    master = cria_interface()
    app = Application(master)
    app.mainloop()

main()
