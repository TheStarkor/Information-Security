from utils import mod


class Fiat(object):
    def __init__(self, r, s, n):
        self.r = r
        self.s = s
        self.n = n
        self.x = mod(self.r, 2, self.n)
        self.v = mod(self.s, 2, self.n)
        print(f"n = {n}, s = {s}, r = {r}")
        print(f"x = {self.x}, v = {self.v}")

    def first(self, e):
        self.e = e
        self.y = (self.r * ((self.s) ** self.e)) % self.n

        print(f"y = {self.y}")

    def verify(self):
        new = mod(self.y, 2, self.n)
        old = (self.x * mod(self.v, self.e, self.n)) % self.n

        print(f"{new} ?= {old}")


if __name__ == "__main__":
    fiat = Fiat(16, 12, 77)
    fiat.first(1)
    fiat.verify()
