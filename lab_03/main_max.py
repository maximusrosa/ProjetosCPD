"""Implementação do algoritmo MSD Radix Sort"""

import collections

# Utility function to get the ASCII value of the character at index d in the string
def char_at(string, d):
    if len(string) <= d:
        return -1
    else:
        return ord(string[d])

# Function to sort the array using MSD Radix Sort recursively
def MSD_sort(string_list, lo, hi, d):
    # Recursive break condition
    if hi <= lo:
        return

    # Stores the ASCII Values
    count = [0] * (256 + 1)

    # Temp is created to easily swap strings in str[]
    temp = collections.defaultdict(str)

    # Store the occurrences of the most significant character from each string in count[]
    for i in range(lo, hi+1):
        c = char_at(string_list[i], d)
        temp[count[c]] = string_list[i]
        count[c] += 1

    # Change count[] so that count[] now contains actual position of this digits in temp[]
    for r in range(256):
        count[r + 1] += count[r]

    # Build the temp
    for i in range(lo, hi+1):
        c = char_at(string_list[i], d)
        temp[count] = string_list[i]
        count += 1

    # Copy all strings of temp to str[], so that str[] now contains partially sorted strings
    for i in range(lo, hi+1):
        string_list[i] = temp[i - lo]

    # Recursively MSD_sort() on each partially sorted strings set to sort them by their next character
    for r in range(256):
        MSD_sort(string_list, lo + count[r], lo + count[r + 1] - 1, d + 1)

# Function to print an array
def print_list(string_list):
    for i in string_list:
        print(i, end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    # Input String
    string_list = ["midnight", "badge", "bag", "worker", "banner", "wander"]

    # Size of the string
    n = len(string_list)

    print("Unsorted array : ", end="")

    # Print the unsorted array
    print_list(string_list)

    # Function Call
    MSD_sort(string_list, 0, n - 1, 0)

    print("Sorted array : ", end="")

    # Print the sorted array
    print_list(string_list)
