# Informações Relevantes:
# 0 < num_strings ≤ 100
# 0 < tam_strings ≤ 50

def main():
    with open("Sample Input.txt", "r") as file:
        # Estruturação das informações do dataset
        num_datasets = int(file.readline())

        file.read(1)  # pulando o '\n'

        inf_dataset = file.readline().rstrip('\n').split(' ')
        tam_strings = int(inf_dataset[0])
        num_strings = int(inf_dataset[1])

        lst_seq_dna = le_dataset(file, num_strings)

    for lst in lst_seq_dna:
        print(lst)


def le_dataset(file, num_strings):
    lst_seq_dna = []
    for i in range(num_strings):
        lst_seq_dna.append(split((file.readline().rstrip('\n'))))

    return lst_seq_dna


def split(word):
    return list(word)


if __name__ == '__main__':
    main()
