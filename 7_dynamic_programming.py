def test_grasshopper_count_routes():
    """
        Test grasshopper_count_routes
    :return: None
    """
    print("Test grasshopper_count_routes #1: ", end='')
    print("OK") if grasshopper_count_routes(2) == 1 else print("Failed")
    print("Test grasshopper_count_routes #2: ", end='')
    print("OK") if grasshopper_count_routes(4) == 6 else print("Failed")


def grasshopper_count_routes(n):
    """
        A grasshopper is at 1.
    It can make a move  only at +1, +2 or +3.
    How many routes are exist to reach point N?
    Recursive function is:
               |F(n-1) + F(n-2) + F(n-3)
               |F(0) = 0
        F(n) = |F(1) = 1
               |F(2) = 2
    :param n: int N points
    :return: int number of routes
    """
    assert n > 0, "N must be greater than 0"
    f = [0, 1, 2]
    if n < 3:
        return f[n-1]
    for i in range(3, n+1):
        f[i % 3] = f[0] + f[1] + f[2]
    return f[i % 3]


def test_grasshopper_find_min():
    """
        Test test_grasshopper_find_min
    :return: None
    """
    print("Test test_grasshopper_find_min #1: ", end='')
    print("OK") if grasshopper_find_min(3) == 1 else print("Failed")
    print("Test test_grasshopper_find_min #2: ", end='')
    print("OK") if grasshopper_find_min(6) == 3 else print("Failed")
    print("Test test_grasshopper_find_min #3: ", end='')
    print("OK") if grasshopper_find_min(7) == 3 else print("Failed")


def grasshopper_find_min(n):
    """
        A grasshopper is at 1.
    It can make a move  only at +1 or +2.
    What is the minimum number of jumps required to reach point N
    Recursive function is:
               |min(C(n-1), C(n-2)) + 1
        C(n) = |C(0) = 0
               |C(1) = 0
    :param n: int N points
    :return: int minimum number of jumps
    """
    assert n > 0, "N must be greater than 0"
    c = [0, 0]
    if n < 2:
        return 0
    for i in range(2, n+1):
        c[i % 2] = min(c[0], c[1]) + 1
    return c[i % 2]


def test_grasshopper_cheapest_route():
    """
        Test grasshopper_cheapest_route
    :return: None
    """
    allowed = [True, True, True, True, True, True, True]
    price = [0, 0, 1, 2, 3, 4, 5]
    print("Test grasshopper_cheapest_route #1: ", end='')
    if grasshopper_cheapest_route(6, allowed, price) == 9:
        print("OK")
    else:
        print("False")
    allowed = [True, True, True, True, False, True, True]
    price = [0, 0, 1, 2, 3, 4, 5]
    print("Test grasshopper_cheapest_route #2: ", end='')
    if grasshopper_cheapest_route(6, allowed, price) == 11:
        print("OK")
    else:
        print("False")


def grasshopper_cheapest_route(n: int, allowed: list, price: list):
    """
        A grasshopper is at 1.
    It can make a move  only at +1 or +2.
    Visit each single point costs "price"
    What is the cheapest cost required to reach point N
    Recursive function is:
               |price(n) + min(C(n-1), C(n-2))
        C(n) = |C(0) = 0
               |C(1) = 0
               |C(not allowed) = inf
    :param n: int N points
    :param allowed: list of booleans, means points allowed for visiting
    :param price: list cost of visiting each single point
    :return: int cheapest cost
    """
    assert n > 0, "N must be greater than 0"
    if n < 3:
        return 0
    c = [0, 0] + [float("inf")]*(n-1)
    for i in range(2, n+1):
        if allowed[i]:
            c[i] = price[i] + min(c[i-1], c[i-2])
    return c[-1]


def test_chess_rook_find_min():
    """
        Test chess_rook_find_min
    :return: None
    """
    print("Test chess_rook_find_min: ", end='')
    print("OK") if chess_rook_find_min(4, 4) == 6 else print("Failed")


def chess_rook_find_min(n: int, m: int):
    """
        A chess rook is placed on chess board size of N*M
    The rook can make only 1 step horizontally or vertically for 1 move
    What minimal number of moves required to reach point (N,M)?
                        |R|_|_|_|
                        |_|_|_|_|
                        |_|_|_|_|
                        |_|_|_|x|
    Recursive function is:
                 | min(F(n-1,m); F(n,m-1) + 1
                 | 0, n=1 & m=1
        F(n,m) = | m, F(0,m)
                 | n, F(0,n)
    :param n: int number of vertically cells
    :param m: int number of horizontally cells
    :return: int minimal number of moves
    """
    f = [[(n+m) if n*m == 0 else 0 for m in range(m+1)] for n in range(n+1)]
    f[1][1] = 0
    for n in range(1, n+1):
        for m in range(1, m+1):
            if n*m == 1:
                continue
            f[n][m] = min(f[n-1][m], f[n][m-1]) + 1
    return f[-1][-1]


def test_chess_rook_count_routes():
    """
        Test chess_rook_count_routes
    :return: None
    """
    print("Test chess_rook_count_routes: ", end='')
    print("OK") if chess_rook_count_routes(4, 4) == 20 else print("Failed")


def chess_rook_count_routes(n: int, m: int):
    """
        A chess rook is placed on chess board size of N*M
    The rook can make only 1 step horizontally or vertically for 1 move
    What number of routes is exist to reach point (N,M)?
                        |R|_|_|_|
                        |_|_|_|_|
                        |_|_|_|_|
                        |_|_|_|x|
    Recursive function is:
                 | F(n-1,m) + F(n,m-1)
                 | 1, n=1 & m=1
        F(n,m) = | 0, F(0,m)
                 | 0, F(0,n)
    :param n: int number of vertically cells
    :param m: int number of horizontally cells
    :return: int number of existing routes
    """
    f = [[0]*(m+1) for n in range(n+1)]
    f[1][1] = 1
    for n in range(1, n+1):
        for m in range(1, m+1):
            if n*m == 1:
                continue
            f[n][m] = f[n-1][m] + f[n][m-1]
    return f[-1][-1]


def test_lcs():
    """
        Test largest common subsequence
    :return: None
    """
    print("Test lcs: ", end='')
    print("OK") if lcs("ABCDEFG", "BEG34") == 3 else print("Failed")


def lcs(a, b):
    """
        Let's define function of length for lcs:
         a  :=> [a(1), a(2), a(3) ...a(n-1), a(n)]
         b  :=> [b(1), b(2), b(3) ...b(m-1), b(m)]

                 | F(n-1, m-1) + 1, a(n) = b(n)
        F(n,m) = | max(F(n-1,m); F(n,m-1)), a(n) != b(n)
                 | 0, F(0,m)
                 | 0, F(n,0)
    :param a: str or list
    :param b: str or list
    :return: int length of largest common subsequence
    """
    n = len(a)
    m = len(b)
    f = [[0]*(m+1) for n in range(n+1)]
    for n in range(1, n+1):
        for m in range(1, m+1):
            if a[n-1] == b[m-1]:
                f[n][m] = f[n-1][m-1] + 1
            else:
                f[n][m] = max(f[n-1][m], f[n][m-1])
    return f[-1][-1]


if __name__ == '__main__':
    test_grasshopper_count_routes()
    test_grasshopper_find_min()
    test_grasshopper_cheapest_route()
    test_chess_rook_find_min()
    test_chess_rook_count_routes()
    test_lcs()