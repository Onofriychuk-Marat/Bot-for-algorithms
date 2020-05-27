# В данном файле лежат все алгоритмы

def gcd(a=30, b=100):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(a, b - a)


def recheto(size=100):
    a = [x for x in range(size + 1)]

    a[1] = i = 0
    while i <= size:
        if a[i] != 0:
            j = i + i
            while j <= size:
                a[j] = 0
                j = j + i
        i += 1

    res = list(set(a) - {0})
    res.sort()
    return res


def pow(a=2, n=10):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a ** 2, n / 2)
    else:
        return pow(a, n - 1) * a


mas = []


def bin_next(m, prefix=""):
    if m == 0:
        mas.append(prefix)
        return
    bin_next(m - 1, prefix + "0")
    bin_next(m - 1, prefix + "1")


def bin(m=5):
    global mas
    mas = []
    bin_next(m)
    return mas


def generator_next(n, m, prefix=''):
    if m == 0:
        mas.append(prefix)
        return
    prefix = prefix or ''
    for digit in range(n):
        if not str(digit) in prefix:
            prefix += str(digit)
            generator_next(n, m - 1, prefix)
            prefix = prefix[:-1]


def generator(n=3, m=3):
    global mas
    mas = []
    generator_next(n, m)
    return mas


def decomposition_next(x):
    global mas
    divisor = 2

    while x != 1:
        if x % divisor == 0:
            mas.append(divisor)
            x /= divisor
        else:
            divisor += 1


def decomposition(x=100):
    global mas
    mas = []
    decomposition_next(x)
    return mas


def insert_sort(mas=[3, 1, 5, 2, 4]):
    size = len(mas)
    for i in range(1, size):
        k = i
        while k > 0 and mas[k] < mas[k - 1]:
            mas[k], mas[k - 1] = mas[k - 1], mas[k]
            k -= 1
    return mas


def choice_sort(mas=[3, 1, 5, 2, 4]):
    size = len(mas)
    for i in range(0, size - 1):
        for k in range(i + 1, size):
            if mas[i] > mas[k]:
                mas[i], mas[k] = mas[k], mas[i]
    return mas


def bubble_sort(mas=[3, 1, 5, 2, 4]):
    size = len(mas)
    for i in range(1, size):
        for k in range(0, size - i):
            if mas[k] > mas[k + 1]:
                mas[k], mas[k + 1] = mas[k + 1], mas[k]
    return mas


def tom_choara(A=None):
    if A is None:
        A = [1, 9, 4, 8, 2, 3, 7, 5, 3, 5, 6, 0]
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for i in A:
        if i < barrier:
            L.append(i)
        elif i == barrier:
            M.append(i)
        else:
            R.append(i)
    tom_choara(L)
    tom_choara(R)
    k = 0
    for i in L + M + R:
        A[k] = i
        k += 1
    return A


def right_search(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right - 1


def left_search(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left + 1


def bin_search(a=None, key=4):
    if a is None:
        a = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7]
    return left_search(a, key), right_search(a, key)


def kuznechick(n=8, list_stat=None):
    if list_stat is None:
        list_stat = [True, True, True, True, False, False, True, False, True]
    a = [0, 1, int(list_stat[0])] + [0] * (n - 2)
    for i in range(3, n + 1):
        if list_stat[i]:
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]
    return a[n]


def cheap_trip(n=7, list_price=None):
    if list_price is None:
        list_price = [1, 1, 1, 5, 1, 5, 1, 1]
    good_price = {}
    c = [list_price[1], list_price[1] + list_price[2]] + [0] * (n - 1)
    good_price[1] = list_price[1]
    good_price[2] = list_price[1] + list_price[2]
    for i in range(2, n + 1):
        c[i] = list_price[i] + min(c[i - 1], c[i - 2])
        good_price[i - 1 if c[i - 1] < c[i - 2] else i - 2] = c[i]
    return c[n]


def lcs(A=None, B=[3, 4, 5]):
    if A is None:
        A = [2, 3, 8, 4, 5, 1, 2, 3, 24]
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


def gis(a=None):
    if a is None:
        a = [0, 0, 0, 0, 8, 9, 1, 2, 3, 6, 10, 0, 9, 10, 11]
    f = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        m = 0
        for j in range(0, i):
            if a[i - 1] > a[j] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    return f[len(a)]


def levenstein(a='моlоkо', b='волоко'):
    f = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[len(a)][len(b)]


def prefix_sufix(a):
    p = [0] * len(a)
    size_a = len(a)
    j = 0
    i = 1

    while i < size_a:
        if a[i] == a[j]:
            j += 1
            p[i] = j
            i += 1
        elif j == 0:
            i += 1
        else:  # j != 0
            j = p[j - 1]
    return p


def knut_moris_prat(a='abbaabbabcccccccabbaabbab', sub='abbaab'):
    p = prefix_sufix(sub)
    indices = []
    size_s = len(a)
    size_sub = len(sub)
    i = 0
    j = 0

    while i < size_s:
        if j == size_sub:
            indices.append(i - j)
            j = 0
        elif a[i] == sub[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = p[j - 1]
    return indices
