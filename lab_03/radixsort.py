# insertion sort a[lo..hi], starting at dth character
def insertion_sort(a, lo, hi, d):
    for i in range(lo, hi + 1):
        j = i
        while j > lo and less(a[j], a[j-1], d):
            exch(a, j, j-1)
            j -= 1

# exchange a[i] and a[j]
def exch(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# is v less than w, starting at character d
def less(v, w, d):
    for i in range(d, min(len(v), len(w))):
        if v[i] < w[i]:
            return True
        if v[i] > w[i]:
            return False
    return len(v) < len(w)


def char_at(s, d):
    if d == len(s):
        return -1
    return ord(s[d])

def insertion(a, lo, hi, d):
    for i in range(lo, hi + 1):
        j = i
        while j > lo and a[j][d:] < a[j - 1][d:]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

def MSD_sort(a, lo, hi, d, aux):
    R = 256  # ASCII table size
    CUTOFF = 15  # Cutoff for insertion sort

    # cutoff to insertion sort for small subarrays
    if hi <= lo + CUTOFF:
        insertion(a, lo, hi, d)
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

def sort(a):
    n = len(a)
    aux = [None] * n
    MSD_sort(a, 0, n - 1, 0, aux)