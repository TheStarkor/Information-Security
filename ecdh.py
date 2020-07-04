from utils import exeu


class ECDH(object):
    def __init__(self, p, a, b, g_x, g_y, n):
        self.p = p
        self.a = a
        self.b = b
        self.g_x = g_x
        self.g_y = g_y
        self.get_g()
        # self.n = self.get_n()
        self.n = n
        print(f"y^2 = x^3 + {a}x + {b} (mod {p}), G = {g_x, g_y}, order n = {self.n}")
        for n, i in enumerate(self.g):
            print(f"{n} * P = {i[0], i[1]}")

    def get_g(self):
        self.g = [[-1, -1], [self.g_x, self.g_y]]
        x, y = self.same(self.g[1][0], self.g[1][1])
        self.g.append([x, y])
        print(self.g)
        for i in range(3, 50):
            x, y = self.diff(
                self.g[1][0], self.g[1][1], self.g[i - 1][0], self.g[i - 1][1]
            )
            self.g.append([x, y])

    def same(self, x, y):
        s = (((3 * (x ** 2)) + self.a) * exeu(2 * y, self.p)) % self.p
        x2g = ((s ** 2) - (2 * x)) % self.p
        y2g = ((s * (x - x2g)) - y) % self.p

        return x2g, y2g

    def diff(self, xp, yp, xq, yq):
        s = ((yp - yq) * exeu(xp - xq, self.p)) % self.p
        x = ((s ** 2) - (xp + xq)) % self.p
        y = ((s * (xp - x)) - yp) % self.p

        return x, y

    def encrypt(self, d):
        return self.g[d][0], self.g[d][1]

    def verify(self, n, g_x, g_y):
        x, y = 0, 0
        if n == 1:
            return g_x, g_y
        x, y = self.same(g_x, g_y)
        if n == 2:
            return x, y

        for i in range(3, n + 1):
            x, y = self.diff(x, y, g_x, g_y)

        return x, y


if __name__ == "__main__":
    p, a, b = 11, 1, 6
    ecdh = ECDH(p, a, b, 2, 7, 13)  # p, a, b, g_x, g_y, n
    b_x, b_y = ecdh.encrypt(9)
    a_x, a_y = ecdh.encrypt(3)
    print(f"Bob: {b_x, b_y}, Alice: {a_x, a_y}")
    b = ecdh.verify(9, a_x, a_y)
    a = ecdh.verify(3, b_x, b_y)
    print(f"Bob: {b[0], b[1]}, Alice: {a[0], a[1]}")

# xp, yp, xq, yq = 2, 7, 3, 5

# tmp = exeu(xp - xq, 11)
# s = ((yp - yq) * tmp) % 11
# xr = ((s ** 2) - xp - xq) % 11
# yr = ((-yp) + (s * (xp - xr))) % 11
# print(tmp, s, xr, yr)

# temp = exeu(2 * yp, 11)
# s = (((3 * (xp ** 2)) + 1) * (temp)) % 11
# xr = ((s ** 2) - (2 * xp)) % 11
# yr = ((-yp) + (s * (xp - xr))) % 11
# print(temp, s, xr, yr)
