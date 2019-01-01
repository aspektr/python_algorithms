def inp():
    """
        Getting a natural number from keyboard
    :return: None
    """
    print("="*45)
    print("Sieve of Eratosthenes")
    print("="*45)
    print("Please, enter a natural number:", end='')
    return int(input())


def sieve(n: int):
    """
        Returns a boolean array of size n,
    in which True means a prime number.
    An element with the index 0 means a natural number 1
    :param n: int
    :return: list of booleans
    """
    a = [True] * n
    a[0] = False
    for i in range(2, n // 2):
        if a[i-1]:
            for k in range(2, n // i + 1):
                a[k * i - 1] = False
    return a


def count_primes(a: list):
    """
        Count number of prime numbers
    :param a: list
    :return: int, number of prime numbers
    """
    t = 0
    for i in a:
        t += 1 if i else 0
    return t


def count_digits(a: list):
    """
        Count digits in prime numbers
    :param a: list of boolean
    :return: list of frequencies
    """
    # get normal integers instead of boolean list
    primes = [i for i in range(len(a)) if a[i]]
    # get digits from each prime number
    digits = []
    for number in primes:
        digits += [int(i) for i in str(number)]
    # get list of frequencies
    frequencies = [0]*10
    for digit in digits:
        for i in range(0,10):
            if digit == i:
                frequencies[i] += 1
                break
    return frequencies


def print_prime_numbers(a: list, slice: int, cnt: int):
    """
        Print prime numbers to stdout
    :param a: list of booleans
    :param slice: int how many numbers will be shown
    :param cnt: int number of prime numbers in a list
    :return: None
    """
    slice = cnt if slice > cnt else slice
    print("There are last {} prime numbers:".format(slice))
    print([i+1 for i in range(len(a)) if a[i]][-slice:])


def print_number_primes(n: int, rng: int):
    """
        Print number of prime numbers to stdout
    :param n: int number of prime numbers
    :param rng: a range in which primes were searched
    :return: None
    """
    print("Number of prime numbers (<{}):".format(rng), n)


def test_sieve():
    """
        Test sieve function
    """
    print("Test sieve: ", end='')
    a = [False,   # 1
         True,   # 2
         True,   # 3
         False,  # 4
         True,   # 5
         False,  # 6
         True,   # 7
         False,  # 8
         False,  # 9
         False   # 10
         ]
    print("OK") if sieve(10) == a else print("Failed")


def test_count_primes():
    """
        Test count_primes function
    """
    print("Test count_primes: ", end='')
    a = [True,   # 1
         True,   # 2
         True,   # 3
         False,  # 4
         True,   # 5
         False,  # 6
         True,   # 7
         False,  # 8
         False,  # 9
         False   # 10
         ]
    print("OK") if count_primes(a) == 5 else print("Failed")


def test_count_digits():
    print("Test count_digits: ", end='')
    a = [False]*130
    a[1] = True
    a[2] = True
    a[9] = True
    a[11] = True
    a[13] = True
    a[12] = True
    a[21] = True
    a[92] = True
    a[129] = True
    # [1, 2, 9, 11, 13, 12, 21, 92, 129]
    ans = [0,  # 0
           7,  # 1
           5,  # 2
           1,  # 3
           0,  # 4
           0,  # 5
           0,  # 6
           0,  # 7
           0,  # 8
           3]  # 9
    (print("OK") if count_digits(a) == ans
        else print("Failed"))


if __name__ == '__main__':
    # how many numbers will be shown
    slice = 10

    test_sieve()
    test_count_primes()
    test_count_digits()

    n = inp()
    a = sieve(n)
    cnt = count_primes(a)

    print_number_primes(cnt, n)
    print_prime_numbers(a, slice, cnt)
