from hash_table import HashTable

def main():
    tamanho = 7993

    hash_table = HashTable(tamanho)
    hash_table.fill('../data/players.csv')


main()
