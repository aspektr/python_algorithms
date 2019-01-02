def print_header():
    """
        Print main menu header
    :return: None
    """
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
        if n >= 0:
            return n
        else:
            return get_inp_factorial()
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
    return b if a % b == 0 else gcd(b, a//b)


def main_screen_show():
    """
        Recursively show main menu, while exit is not chosen
    :return: None
    """
    option = algo_selection(algos)
    if option == 1:
        print_factorial()
        main_screen_show()
    if option == 5:
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


if __name__ == '__main__':
    test_factorial()
    test_gcd()

    algos = ('Factorial',
             'Euclidean algorithm',
             'Exponentiation by squaring (fast exponentiation)',
             'Tower of Hanoi',
             'Exit'
             )

    main_screen_show()

