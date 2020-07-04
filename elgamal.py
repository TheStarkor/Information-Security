from utils import mod, exeu


class ElgamalSignature(object):
    def __init__(self, p, g, x):
        self.p = p
        self.g = g
        # self.x = random.randint(1, self.p - 1)
        self.x = x
        self.y = mod(self.g, self.x, self.p)

        print(f"public: p = {self.p}, g = {self.g}, y = {self.y}")
        print(f"private: x = {self.x}")

    def generate(self, m, k):
        # self.k = random.randint(1, self.p - 1)
        self.k = k
        self.r = mod(self.g, self.k, self.p)
        self.ki = exeu(self.k, self.p - 1)
        self.s = ((m - self.x * self.r) * self.ki) % (self.p - 1)

        print(f"generate: r = {self.r}, s = {self.s}, k = {self.k}")

        return self.r, self.s

    def verify(self, m, r, s):
        y_r = mod(self.y, self.r, self.p)
        r_r = mod(self.r, self.s, self.p)
        veri = (y_r * r_r) % self.p
        res = mod(self.g, m, self.p)

        print(f"{veri} ?= {res}")


class ElgamalEncryption(object):
    def __init__(self, p, g, x):
        self.p = p
        self.g = g
        # self.x = random.randint(1, self.p - 1)
        self.x = x
        self.y = mod(self.g, self.x, self.p)

        print(f"public: p = {self.p}, g = {self.g}, y = {self.y}")

    def encrypt(self, m, k):
        # self.k = random.randint(1, self.p - 1)
        self.k = k
        self.c1 = mod(self.g, self.k, self.p)
        self.c2 = (m * mod(self.y, self.k, self.p)) % self.p

        print(f"Encryption: C1 = {self.c1}, C2 = {self.c2}")
        return self.c1, self.c2

    def decrypt(self, c1, c2):
        self.m = (c2 * mod(exeu(c1, self.p), self.x, self.p)) % self.p

        print(f"Decrypt: M = {self.m}")
        return self.m


if __name__ == "__main__":
    # elgamalencryption = ElgamalEncryption(23, 7, 9)
    # c1, c2 = elgamalencryption.encrypt(20, 3)
    # m = elgamalencryption.decrypt(c1, c2)

    elgamalsignature = ElgamalSignature(41, 6, 17)
    r, s = elgamalsignature.generate(33, 3)
    elgamalsignature.verify(33, r, s)
