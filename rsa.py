from utils import gcd, exeu, get_coprime


class RSA(object):
    def __init__(self, p, q, m):
        self.p = p
        self.q = q
        self.m = m
        self.n = p * q
        self.pi = (p - 1) * (q - 1)
        self.e = get_coprime(self.pi)
        self.d = exeu(self.e, self.pi)

        print(f"(n, pi) = ({self.n}, {self.pi})")
        print(f"(e, d) = ({self.e}, {self.d})")

    def encryption(self, e):
        m = self.m
        n = self.n

        c = 1
        while e != 0:
            while e % 2 == 0:
                e = e // 2
                m = (m * m) % n
            e -= 1
            c = (c * m) % n

        self.c = c
        return self.c

    def decryption(self, d):
        c = self.c
        n = self.n

        m = 1
        while d != 0:
            while d % 2 == 0:
                d = d // 2
                c = (c * c) % n
            d -= 1
            m = (m * c) % n

        return m


if __name__ == "__main__":

    tests = [[109, 127, 1234]]

    for n, (p, q, m) in enumerate(tests):

        print("======================================================")
        print("No.{} (p={}, q={}, M={})\n".format(n + 1, p, q, m))
        rsa = RSA(p, q, m)
        print("C =", rsa.encryption(rsa.e), end="\n\n")
        print("M =", rsa.decryption(rsa.d))
        print("======================================================\n")
