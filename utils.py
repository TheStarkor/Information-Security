# a * res mod b = 1
# res 는 a 곱셈의 역원
def exeu(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1, t2 = t2, t

    return (s1 + b) % b


# a ** b % p
def mod(c, d, n):
    res = 1
    while d != 0:
        while d % 2 == 0:
            d = d // 2
            c = (c * c) % n
        d -= 1
        res = (res * c) % n

    return res


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def get_order(n):
    res = 0
    for i in range(n):
        if gcd(i, n) == 1:
            res += 1

    return res


def get_orders(n):
    res = []
    for i in range(n):
        if gcd(i, n) == 1:
            res.append(i)

    return res


def is_prime(n):
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k * 2 :: k] = [False] * ((n - k) // k)

    return (lambda x: True if seive[x] else False)(n)


def get_coprime(n):
    res = 2
    while gcd(res, n) != 1:
        res += 1

    return res


def get_generatives(p):
    res = []
    for i in range(2, p):
        if is_primitive(i, p):
            res.append(i)

    return res


def is_primitive(n, p):
    check = [False for i in range(p)]
    check[0] = True

    for i in range(0, p - 1):
        check[mod(n, i, p)] = True

    for i in check:
        if not i:
            return False

    return True


# "1234" -> [1, 2, 3, 4]
def intstr_to_list(s):
    return list(map(int, s))


def list_to_intstr(s):
    return "".join(list(map(str, s)))


# abcd -> [0, 1, 2, 3]
def str_to_list(s):
    return list(map(lambda c: ord(c) - ord("a"), s))


# [0, 1, 2, 3] -> abcd
def list_to_str(s):
    return "".join(list(map(lambda c: chr(c + ord("a")), s)))


def calc(l):
    res = []
    for i in l:
        res.append(mod(3, i, 101))
    return res


if __name__ == "__main__":
    # print(get_order(8))
    # print(get_order(7))
    # print(is_prime(5))
    print(get_generatives(101))
    # print(get_generatives(41))
    # l = get_orders(100)
    # # print(l)
    # res = calc(l)
    # # res.sort()
    # print(res)
    # print(len(res))
    # print(exeu(3, 40))
    # print(gcd((3 ** 15) - 1, 77))
