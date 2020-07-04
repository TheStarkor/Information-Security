from utils import (
    exeu,
    get_coprime,
    intstr_to_list,
    str_to_list,
    list_to_str,
    list_to_intstr,
)


class Caesar(object):
    def __init__(self, k):
        self.k = k

    def encrypt(self, m):
        res = []
        for i in m:
            res.append((i + self.k) % 26)
        return res

    def decypt(self, c):
        res = []
        for i in c:
            res.append((i - self.k) % 26)
        return res


class Affine(object):
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2

    def encrypt(self, m):
        res = []
        for i in m:
            res.append(((i - self.k2 + 26) * exeu(self.k1, 26)) % 26)
        return res

    def decrypt(self, c):
        res = []
        for i in c:
            res.append(((i - self.k2 + 26) * exeu(self.k1, 26)) % 26)
        return res


class Vigenere(object):
    def __init__(self, k, p):
        self.k = k
        self.p = p

    def encrypt(self, m):
        res = []
        for i in range(len(m)):
            j = i % len(self.k)
            res.append((m[i] + self.k[j]) % self.p)
        return res

    def decrypt(self, c):
        res = []
        for i in range(len(c)):
            j = i % len(self.k)
            res.append((c[i] - self.k[j]) % self.p)
        return res


if __name__ == "__main__":
    enc = str_to_list("wegvrjepqnwezbdzqetgzbigvpta")
    affine = Affine(exeu(5, 26), 13)
    res = affine.decrypt(enc)
    res = list_to_str(res)
    print(res)

    key = intstr_to_list("20170317")
    vigenere = Vigenere(key, 10)
    m = intstr_to_list("314159265358979323846264")
    res = vigenere.encrypt(m)
    res = list_to_intstr(res)
    print(res)
