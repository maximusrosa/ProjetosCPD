from src.hash_table import HashTable, get_minirating_info
from src.interface import Application, cria_interface

from time import time
from collections import namedtuple

# Constantes
ID = '130642' # id do usuário com mais avaliações
TAMANHO_TABELA = 7993

Avaliacao = namedtuple('Avaliacao', ['player_id', 'nota'])

def main():
    players_ht = HashTable(TAMANHO_TABELA)
    users_ht = HashTable(TAMANHO_TABELA)

    start = time()
    players_ht.get_players_info()
    get_minirating_info(players_ht, users_ht)
    players_ht.update_global_ratings()
    end = time()

    print(f'Tempo de construção das tabelas: {end - start:.2f} segundos ou {(end - start) * 1000:.2f} milisegundos')

    # Ex: Procurando o Messi
    #print(str(players_ht.get("158023")))

    # pras pesquisas, ainda temos que decidir quais algoritmos de ordenação usar

    # Pesquisa 2: jogadores revisados por usuários
    print(users_ht.get(ID).get_top_rated_players(players_ht))

    # Pesquisa 3: melhores jogadores de uma determinada posição
    print(players_ht.get_top_players_by_position("ST", 10))


    # Salvando os tabelas
    with open('output/players_ht.txt', 'w') as file:
        file.write(str(players_ht))

    #with open('output/users_ht.txt', 'w') as file:
    #    file.write(str(users_ht))

    master = cria_interface()
    app = Application(master)
    app.mainloop()

main()
