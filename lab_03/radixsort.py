from collections import Counter


def char_at(s, d):
    if d == len(s):
        return -1
    return ord(s[d])

# insertion sort a[lo..hi], starting at dth character
def insertion_sort(a, lo, hi, d):
    for i in range(lo, hi + 1):
        j = i
        while j > lo and a[j][d:] < a[j - 1][d:]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def MSD_sort(a, lo, hi, d, aux):
    R = 256      # ASCII table size
    CUTOFF = 15  # Cutoff for insertion sort

    # cutoff to insertion sort for small subarrays
    if hi <= lo + CUTOFF:
        insertion_sort(a, lo, hi, d)
        return

    # compute frequency counts
    count = [0] * (R + 2)
    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        count[c + 2] += 1

    # transform counts to indicies
    for r in range(R + 1):
        count[r + 1] += count[r]

    # distribute
    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        aux[count[c + 1]] = a[i]
        count[c + 1] += 1

    # copy back
    for i in range(lo, hi + 1):
        a[i] = aux[i - lo]

    # recursively sort for each character (excludes sentinel -1)
    for r in range(R):
        MSD_sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1, aux)


# 1.1 Implementar o algoritmo de ordenação Radix Sort MSD para strings
def radixsort(a):
    n = len(a)
    aux = [None] * n
    MSD_sort(a, 0, n - 1, 0, aux)


def main():

# ---------------- Frankenstein ---------------- #

    with open("frankestein.txt", "r") as input_file:
        words = input_file.read().split() 


    # 1.2: Ordenar palavras de um arquivo de entrada usando Radix Sort MSD
    radixsort(words)

    with open("frankestein_sorted.txt", "w") as output_file:
        for word in words:
            output_file.write(f"{word}\n")


    # 1.3: Contar as palvras do arquivo ordenado
    word_counts = Counter(words)    # cria um dicionário (hash table) com as palavras como índices e suas frequências como valores
    
    with open("frankestein_counted.txt", "w") as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word} {count}\n")

    print("Arquivo 1.3 criado com sucesso!")


    # 1.4: Top 1000 palavras mais frequentes
    with open("frankestein_ranked.txt", "w") as output_file:
        for word, count in word_counts.most_common(1000):
            output_file.write(f"{word} {count}\n")

    print("Arquivo 1.4 criado com sucesso!")


# ---------------- War and Peace ---------------- #

    with open("war_and_peace.txt", "r") as input_file:
        words = input_file.read().split() 


    # 1.2: Ordenar palavras de um arquivo de entrada usando Radix Sort MSD
    radixsort(words)

    with open("war_and_peace_sorted.txt", "w") as output_file:
        for word in words:
            output_file.write(f"{word}\n")


    # 1.3: Contar as palvras do arquivo ordenado
    word_counts = Counter(words) 
    
    with open("war_and_peace_counted.txt", "w") as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word} {count}\n")

    print("Arquivo 1.3 criado com sucesso!")


    # 1.4: Top 1000 palavras mais frequentes
    with open("war_and_peace_ranked.txt", "w") as output_file:
        for word, count in word_counts.most_common(1000):
            output_file.write(f"{word} {count}\n")

    print("Arquivo 1.4 criado com sucesso!")



if __name__ == '__main__':
    main()

# Material utilizado como referência: https://algs4.cs.princeton.edu/51radix/MSD.java.html