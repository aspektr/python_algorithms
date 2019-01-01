def insertion_sort(a: list):
    """
        Realizes insertion sort
    :param a: list of int
    :return: None
    """
    n = len(a)
    for i in range(1, n):
        k = i
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1


def selection_sort(a: list):
    """
        Realize selection sort
    :param a: list on int
    :return: None
    """
    n = len(a)
    for i in range(0, n-1):
        for k in range(i+1, n):
            if a[k] < a[i]:
                a[i], a[k] = a[k], a[i]


def bubble_sort(a: list):
    """
        Realise bubble sort
    :param a: list of int
    :return: None
    """
    n = len(a)
    for i in range(0, n):
        for k in range(1, n-i):
            if a[k] < a[k-1]:
                a[k], a[k-1] = a[k-1], a[k]


def test_sorting(f: object):
    """
        Test for sorting functions
    :param f: sorting function
    :return: None
    """
    print("Test ", f.__name__, ': ', sep = '', end='')
    a = [1, 5, 3, 4, 1, 2, 6, 6]
    f(a)
    (print("OK") if a == [1, 1, 2, 3, 4, 5, 6, 6]
        else print("Failed"))


if __name__ == '__main__':
    test_sorting(insertion_sort)
    test_sorting(selection_sort)
    test_sorting(bubble_sort)
