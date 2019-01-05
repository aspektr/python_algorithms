def test_qsort():
    """
        Test qsort
    :return: None
    """
    # case 1
    a = [9, 4, 7, 6, 5, 8, 4, 8]
    print("Test case 1 quicksort: ", end='')
    qsort(a)
    print("OK") if a == [4, 4, 5, 6, 7, 8, 8, 9] else print("Failed")
    # case 2
    a = [4, 4, 4, 4, 3, 4, 5, 6]
    print("Test case 2 quicksort: ", end='')
    qsort(a)
    print("OK") if a == [3, 4, 4, 4, 4, 4, 5, 6] else print("Failed")
    # case 3
    a = [4, 4, 4, 4, 4, 4, 4, 4]
    print("Test case 3 quicksort: ", end='')
    qsort(a)
    print("OK") if a == [4, 4, 4, 4, 4, 4, 4, 4] else print("Failed")
    # case 3
    a = [-1, -3, 7, 2, 0, 0, 4, 4]
    print("Test case 4 quicksort: ", end='')
    qsort(a)
    print("OK") if a == [-3, -1, 0, 0, 2, 4, 4, 7] else print("Failed")
    # case 3
    a = [-1, -3, 7, 2, 0, 4, 4]
    print("Test case 5 quicksort: ", end='')
    qsort(a)
    print("OK") if a == [-3, -1, 0, 2, 4, 4, 7] else print("Failed")


def test_partition():
    """
        Test partition
    :return: None
    """
    # case 1
    a = [4, 4, 4, 4, 3, 4, 5, 6]
    print("Test case 1 for partition: ", end='')
    partition(a, len(a)-1, 0)
    print("OK") if a == [4, 3, 4, 4, 4, 4, 5, 6] else print("Failed")
    # case 2
    a = [4, 4, 4, 4, 3, 4, 5]
    print("Test case 2 for partition: ", end='')
    partition(a, len(a)-1, 0)
    print("OK") if a == [4, 3, 4, 4, 4, 4, 5] else print("Failed")


def qsort(a: list, hi: int = None, lo: int = None):
    """
        Realisation of quicksort algorithm.
        Sort list in place.
    :param a: list
    :param hi: right marker
    :param lo: left marker
    :return: None
    """
    if hi is None:
        hi = len(a)-1
    lo = lo or 0
    if hi <= lo:
        return
    bar_hi, bar_lo = partition(a, hi, lo)
    qsort(a, bar_hi, lo)
    qsort(a, hi, bar_lo)


def partition(a: list, hi: int, lo: int):
    """
        Partition takes the value PIVOT of a middle element of the array A,
    and rearranges the values of the elements of the array
    in such a way that all elements < PIVOT move on the left of the PIVOT, and
    all elements > PIVOT move on the right of the PIVOT
    :param a: list A-array
    :param hi: int right marker
    :param lo: int left marker
    :return: tuple<int> right and left markers
    """
    pivot = a[(hi+lo)//2]
    while lo <= hi:
        while a[lo] < pivot:
            lo += 1
        while a[hi] > pivot:
            hi -= 1
        if lo <= hi:
            a[lo], a[hi] = a[hi], a[lo]
            lo, hi = lo + 1, hi - 1
    return hi, lo


def inp(stop: list, a=[], user_input=None):
    """
        Handle user input
    :param stop: list stop-commands (for instance, stop)
    :param a: list of elements for sorting
    :param user_input:str or float
    :return: None
    """
    if user_input in stop:
        print("Starting sort...")
        qsort(a)
        print("Done! Sort list is: ", a)
        print("Let's try again!")
        inp(stop, a=[])
    print("Your list now is: ",a)
    print("Please, add number:")
    try:
        x = input()
    except EOFError:
        print("Shutting down...")
        raise SystemExit(0)
    try:
        a.append(float(x))
        inp(stop, a, x)
    except:
        inp(stop, a, x)


if __name__ == '__main__':
    print("Divide and conquer!")
    test_qsort()
    test_partition()
    stop_command = ['q', 'quite', 'exit', 'exit()', 'quite()', 'stop']
    inp(stop=stop_command)
