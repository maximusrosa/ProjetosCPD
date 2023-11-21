"""
Implementação do algoritmo quicksort utilizando os particionamentos de Hoare e Lomuto com duas escolhas de particionador:
Mediana de 3 e Escolha Aleatória

Informações da saída: tamanho da entrada, número de trocas, número de chamadas recursivas, tempo de execução
"""

import hoare
import lomuto
from time import perf_counter


def salva_resultados(particionamento, escolha_pivo):
    output_file = open(f"stats-{escolha_pivo}-{particionamento}.txt", "w")

    with open("entrada-quicksort.txt", "r") as input_file:
        if particionamento == "hoare":
            for linha in input_file:
                lista_num = list(map(int, linha.split()))
                tam_lista = lista_num.pop(0)

                hoare.swaps = hoare.rec_count = 0

                start_time = perf_counter()
                hoare.quicksort(lista_num, 0, tam_lista - 1, escolha_pivo)
                end_time = perf_counter()
                elapsed_time = (end_time - start_time) * 1000

                output_file.write(f"TAMANHO ENTRADA {tam_lista}\n"
                                  f"SWAPS {hoare.swaps}\n"
                                  f"RECURSOES {hoare.rec_count}\n"
                                  f"TEMPO {elapsed_time:.3f}\n")

        elif particionamento == "lomuto":
            for linha in input_file:
                lista_num = list(map(int, linha.split()))
                tam_lista = lista_num.pop(0)

                lomuto.swaps = lomuto.rec_count = 0

                start_time = perf_counter()
                lomuto.quicksort(lista_num, 0, tam_lista - 1, escolha_pivo)
                end_time = perf_counter()
                elapsed_time = (end_time - start_time) * 1000

                output_file.write(f"TAMANHO ENTRADA {tam_lista}\n"
                                  f"SWAPS {lomuto.swaps}\n"
                                  f"RECURSOES {lomuto.rec_count}\n"
                                  f"TEMPO {elapsed_time:.3f}\n")

        else:
            assert False, "Particionamento inválido."

    output_file.close()


def main():
    salva_resultados("hoare", "mediana")
    salva_resultados("hoare", "aleatorio")
    salva_resultados("lomuto", "mediana")
    salva_resultados("lomuto", "aleatorio")

    print("Arquivos de saída gerados com sucesso.")


main()
