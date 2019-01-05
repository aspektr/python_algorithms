def test_lo_bound():
    """
        Test low boundary
    :return: None
    """
    a = [1, 2, 3, 4, 5, 6]
    print("Low boundary test: ", end='')
    print("OK") if lo_bound(a, -1, len(a) + 1, 2) == 0 else print("Failed")


def test_hi_bound():
    """
        Test high boundary
    :return: None
    """
    a = [1, 2, 2, 3, 4, 5, 6]
    print("High boundary test: ", end='')
    print("OK") if hi_bound(a, -1, len(a) + 1, 2) == 3 else print("Failed")


def test_b_search():
    """
        Test binary search
    :return: None
    """
    a = [1, 2, 2, 3, 4, 5, 6]
    print("Binary search test #1: ", end='')
    print("OK") if b_search(a, 2) == (0, 3) else print("Failed")
    a = [1, 1, 2, 3, 4, 5, 6]
    print("Binary search test #2: ", end='')
    print("OK") if b_search(a, 7) == (6, 7) else print("Failed")
    a = [1, 1, 2, 3, 4, 5, 6]
    print("Binary search test #3: ", end='')
    print("OK") if b_search(a, 0) == (-1, 0) else print("Failed")
    a = [1, 1, 2, 3, 4, 5, 6, 10]
    print("Binary search test #4: ", end='')
    print("OK") if b_search(a, 8) == (6, 7) else print("Failed")
    a = [1, 1, 1, 1, 1, 1, 1, 1]
    print("Binary search test #5: ", end='')
    print("OK") if b_search(a, 1) == (-1, 8) else print("Failed")


def b_search(a: list, n: int):
    """
        Realise binary search
    :param a: list
    :param n: sought value
    :return: tuple<int> low boundary and high boundary
    """
    low_boundary = lo_bound(a, -1, len(a), n)
    high_boundary = hi_bound(a, -1, len(a), n)
    return low_boundary, high_boundary


def lo_bound(a: list, lo: int, hi: int, n):
    """
        Find index of low boundary
    :param a: list
    :param lo: int index low boundary
    :param hi: int index high boundary
    :param n: sought value
    :return: int low boundary
    """
    if hi - lo <= 1:
        return lo
    m = (lo + hi)//2  # middle
    return lo_bound(a, m, hi, n) if a[m] < n else lo_bound(a, lo, m, n)


def hi_bound(a: list, lo: int, hi: int, n):
    """
        Find index of high boundary
    :param a: list
    :param lo: int index low boundary
    :param hi: int index high boundary
    :param n: sought value
    :return: int how boundary
    """
    if hi - lo <= 1:
        return hi
    m = (lo + hi)//2  # middle
    return hi_bound(a, lo, m, n) if a[m] > n else hi_bound(a, m, hi, n)


if __name__ == '__main__':
    test_lo_bound()
    test_hi_bound()
    test_b_search()
