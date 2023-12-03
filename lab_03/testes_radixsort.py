from radixsort import insertion_sort, radixsort

def tests_insertion_sort():
    # Test empty list
    a = []
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == []

    # Test single element list
    a = ["a"]
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == ["a"]

    # Test multiple element list
    a = ["cat", "dog", "apple", "banana"]
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == ["apple", "banana", "cat", "dog"]

    # Test list with duplicate elements
    a = ["cat", "dog", "cat", "apple"]
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == ["apple", "cat", "cat", "dog"]

    # Test list with special characters
    a = ["cat!", "dog#", "apple$", "banana%"]
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == ["apple$", "banana%", "cat!", "dog#"]

    # Test list with numbers (as strings)
    a = ["1", "2", "10", "20"]
    insertion_sort(a, 0, len(a)-1, 0)
    assert a == ["1", "10", "2", "20"]  # Strings are sorted lexicographically


import random
import string

def test_radixsort():
    # Generate a list of 1000 random strings, each of random length up to 10
    a = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 10))) for _ in range(1000)]
    
    # Make a copy of the list and sort it using Python's built-in sort
    expected = sorted(a.copy())
    
    # Sort the list using MSD_sort
    radixsort(a)
    
    # Check that the two lists are the same
    assert a == expected

test_radixsort()