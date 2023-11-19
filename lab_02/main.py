import hoare
from time import perf_counter

def salva_resultados(nome_arq, escolha_pivo):
    output_file = open(nome_arq, "w")

    with open("entrada-quicksort.txt", "r") as input_file:
        linhas_arq = input_file.readlines()

        for linha in linhas_arq:
            lista_num = list(map(int, linha.split()))
            tam_lista = lista_num.pop(0)

            output_file.write(f"TAMANHO ENTRADA {tam_lista}\n")

            hoare.swaps = hoare.rec_count = 0

            start_time = perf_counter()
            hoare.quicksort(lista_num, 0, tam_lista - 1, escolha_pivo)
            end_time = perf_counter()
            elapsed_time = (end_time - start_time) * 1000

            output_file.write(f"SWAPS {hoare.swaps}\n"
                              f"RECURSOES {hoare.rec_count}\n"
                              f"TEMPO {elapsed_time:.3f}\n")

    output_file.close()


def main():
    salva_resultados("stats-mediana-hoare.txt", "md3")
    salva_resultados("stats-aleatorio-hoare.txt", "rand")

    print("Arquivos de saída gerados com sucesso.")


main()
