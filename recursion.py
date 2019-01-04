def print_header():
    """
        Print main menu header
    :return: None
    """
    print()
    print("*" * 45)
    print("Please, select algorithm:")
    print("*" * 45)


def print_rules(len: int):
    """
        Print rules, when error in input happened
    :param len: int length of list of algos
    :return: None
    """
    print("Sorry, number must be 1 -", len)
    print("Please, try again...")


def print_list_algos(algos:tuple):
    """
        Print list of algos for choice
    :param algos: tuple of algos
    :return: None
    """
    for i, name_algo in enumerate(algos):
        print("    {} - {}".format(i + 1, name_algo))


def algo_selection(algos: tuple):
    """
    Print list of options and return user choice
    :param algos: tuple of algos
    :return: int user choice
    """
    print_header()
    print_list_algos(algos)
    print("Your choice: ", end='')
    return get_num_algo(algos)


def get_num_algo(algos: tuple):
    """
        Recursively asks user to make choice,
    while input is wrong
    :param algos: tuple of algos
    :return: int user choice
    """
    length = len(algos)
    try:
        n = int(input())
        if n not in range(1, length+1):
            print_rules(length)
            return algo_selection(algos)
        else:
            return n
    except:
        print_rules(length)
        return algo_selection(algos)


def factorial(n: int):
    """
        Recursively count factorial from n
    :param n: int
    :return: int factorial from n
    """
    return 1 if n == 0 else factorial(n-1)*n


def get_inp_factorial():
    """
        Recursively asks user to make choice,
    while input is wrong
    :return: int user input
    """
    print("Please, type n for factorial: ")
    try:
        n = int(input())
        return n if n >= 0 else get_inp_factorial()
    except:
        print("Number must be integer and not negative")
        return get_inp_factorial()


def print_factorial():
    """
        Print result of calculation factorial
    :return: None
    """
    n = get_inp_factorial()
    print(n, "! = ", factorial(n), sep='')


def gcd(a: int, b: int):
    """
        Find grand common divisor for couple numbers a and b
    :param a: int
    :param b: int
    :return: int grand common divisor
    """
    return b if a % b == 0 else gcd(b, a % b)


def get_inp_gcd(cnt='first'):
    """
        Recursively asks user to make choice,
    while input is wrong

    :param cnt: str first or second call
    :return: int user input
    """
    print("Please, type", cnt, "number for Euclidean algorithm: ", end='')
    try:
        n = int(input())
        return n if n > 0 else get_inp_gcd(cnt)
    except:
        print("Number must be integer and positive")
        return get_inp_gcd(cnt)


def print_gcd():
    """
        Print result of calculation gcd
    :return: None
    """
    a = get_inp_gcd()
    b = get_inp_gcd('second')
    print(a, " gcd ", b, " = ", gcd(a,b), sep='')


def pow(a: float, n: int):
    """
        Raises a number A to a power N (fast method)
    :param a: float number
    :param n: int power
    :return: float A^N
    """
    if n == 0:
        return 1
    elif n % 2 == 0:  # power n - even
        return pow(a**2, n//2)
    else:  # power n - odd
        return pow(a, n-1)*a


def get_inp_pow(kind='base'):
    """
        Recursively asks user to make choice,
    while input is wrong

    :param kind: str base or power
    :return: int user input
    """
    print("Please, type", kind, ": ", end='')
    cast = int if kind == 'power' else float
    try:
        n = cast(input())
        if kind == 'power':
            return n if n >= 0 else get_inp_pow(kind)
        else:
            return n
    except:
        print("Power must be integer and not negative")
        print("Base must be float")
        return get_inp_pow(kind)


def print_pow():
    """
        Print result of calculation gcd
    :return: None
    """
    a = get_inp_pow()
    n = get_inp_pow('power')
    print(a, "^", n, " = ", pow(a, n), sep='')


def towers(n: int, from_pile=1, to_pile=2):
    """
        Print orders for replace
    :param n: int number of disks
    :param from_pile: int
    :param to_pile: int
    :return: None
    """
    if n == 1:
        print("Remove 1 disk from {} pile to {} pile"
              .format(from_pile, to_pile))
    else:
        tmp = 6 - from_pile - to_pile
        towers(n-1, from_pile, tmp)
        print("Remove {} disk from {} pile to {} pile"
              .format(n, from_pile, to_pile))
        towers(n-1, tmp, to_pile)


def get_inp_towers():
    """
        Recursively asks user to make choice,
    while input is wrong
    :return: int user input
    """
    print("Please, type quantity of towers: ")
    try:
        n = int(input())
        return n if n >= 0 else get_inp_towers()
    except:
        print("Number must be integer and not negative")
        return get_inp_towers()


def print_towers():
    """
        Run towers function
    :return: None
    """
    n = get_inp_towers()
    towers(n)


def get_inp_permutations():
    """
        Recursively asks user to make choice,
    while input is wrong
    :return: int user input
    """
    print("Please, type number of elements: ")
    try:
        n = int(input())
        return n if n >= 0 else get_inp_permutations()
    except:
        print("Number must be integer and not negative")
        return get_inp_permutations()


def permutations(n: int, m: int = None, prefix: str = ''):
    """
        Print all possible permutations for N elements, be
    careful Number of permutations = n! (factorial)
    :param n: int number of elements for permutations
    :param m: int recursion level
    :param prefix: str output permutation
    :return: None
    """
    m = m or n+1
    if m == 1:
        print(prefix, end=' ')
    for i in range(1, n+1):
        if str(i) not in prefix:
            permutations(n, m - 1, prefix + str(i))


def print_permutations():
    """
        Run permutations function
    :return: None
    """
    n = get_inp_permutations()
    permutations(n)


def show_main_screen():
    """
        Recursively show main menu, while exit is not chosen
    :return: None
    """
    option = algo_selection(algos)
    if option == 1:
        print_factorial()
        show_main_screen()
    if option == 2:
        print_gcd()
        show_main_screen()
    if option == 3:
        print_pow()
        show_main_screen()
    if option == 4:
        print_towers()
        show_main_screen()
    if option == 5:
        print_permutations()
        show_main_screen()
    if option == 6:
        raise SystemExit(0)


def test_factorial():
    """
        Test factorial
    :return: None
    """
    print("Test factorial:", end='')
    print("OK") if factorial(5) == 120 else print("Failed")


def test_gcd():
    """
        Test Euclidean algorithm
    :return: None
    """
    a = 10
    b = 6
    print("Test Euclidean algorithm:", end='')
    print("OK") if gcd(a, b) == 2 else print("Failed")


def test_pow():
    """
        Test pow function
    :return: None
    """
    print("Test pow:", end='')
    print("OK") if pow(2, 10) == 1024 else print("Failed")


if __name__ == '__main__':
    test_factorial()
    test_gcd()
    test_pow()

    algos = ('Factorial',
             'Euclidean algorithm',
             'Exponentiation by squaring (fast exponentiation)',
             'Tower of Hanoi',
             'Permutations',
             'Exit'
             )

    show_main_screen()
