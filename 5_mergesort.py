ext_module = __import__("4_quicksort")


def test_msort():
    """
        Test msort
    :return: None
    """
    # case 1
    a = [9, 4, 7, 6, 5, 8, 4, 8]
    print("Test case 1 merge sort: ", end='')
    msort(a)
    print("OK") if a == [4, 4, 5, 6, 7, 8, 8, 9] else print("Failed")
    # case 2
    a = [4, 4, 4, 4, 3, 4, 5, 6]
    print("Test case 2 merge sort: ", end='')
    msort(a)
    print("OK") if a == [3, 4, 4, 4, 4, 4, 5, 6] else print("Failed")
    # case 3
    a = [4, 4, 4, 4, 4, 4, 4, 4]
    print("Test case 3 merge sort: ", end='')
    msort(a)
    print("OK") if a == [4, 4, 4, 4, 4, 4, 4, 4] else print("Failed")
    # case 4
    a = [-1, -3, 7, 2, 0, 0, 4, 4]
    print("Test case 4 merge sort: ", end='')
    msort(a)
    print("OK") if a == [-3, -1, 0, 0, 2, 4, 4, 7] else print("Failed")
    # case 5
    a = [-1, -3, 7, 2, 0, 4, 4]
    print("Test case 5 merge sort: ", end='')
    msort(a)
    print("OK") if a == [-3, -1, 0, 2, 4, 4, 7] else print("Failed")
    # case 6
    a = [-1, -3, 7, 2, 0, 4, 4]
    print("Test case 6 merge sort: ", end='')
    msort(a, False)
    print("OK") if a == [7, 4, 4, 2, 0, -1, -3] else print("Failed")
    # case 7
    a = [-1, -3, 7, 2, 0, 4, 4]
    uuid = id(a)
    print("Test case 7 merge sort: ", end='')
    msort(a, False)
    print("OK") if uuid == id(a) else print("Failed")


def msort(a: list, ascending=True):
    """
        Realisation of merge sort algorithm
    :param a: list for sort
    :param ascending: boolean
    :return: None
    """
    if len(a) == 1:
        return a
    asc = 2 * ascending - 1
    pivot = len(a)//2
    left = msort(a[:pivot], ascending)
    right = msort(a[pivot:], ascending)
    union = []
    i = k = 0
    while i < len(left) and k < len(right):
        if left[i]*asc <= right[k]*asc:
            union.append(left[i])
            i += 1
        else:
            union.append(right[k])
            k += 1
    union += left[i:] + right[k:]
    for i in range(len(a)):
        a[i] = union[i]
    return a


if __name__ == '__main__':
    test_msort()
    stop_command = ['q', 'quite', 'exit', 'exit()', 'quite()', 'stop']
    ext_module.inp(stop=stop_command, algo=msort)
