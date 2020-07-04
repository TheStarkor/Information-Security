from utils import gcd, mod, exeu, get_coprime


class Blind(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.pi = (p - 1) * (q - 1)
        self.d = get_coprime(self.pi)
        self.e = exeu(self.d, self.pi)

        print(f"Public key: (e, n) = ({self.e}, {self.n})")
        print(f"Private key: (d) = ({self.d})")

    def blinding(self, m):
        self.k = get_coprime(self.n)
        self.blind_m = (m * mod(self.k, self.e, self.n)) % self.n

        print(f"M' = {self.blind_m}")
        return self.blind_m

    def signing(self, blind_m):
        self.blind_s = mod(blind_m, self.d, self.n)

        print(f"S' = {self.blind_s}")
        return self.blind_s

    def unblinding(self, blind_s):
        self.s = (exeu(self.k, self.n) * blind_s) % self.n

        print(f"S = {self.s}")
        return self.s

    def original(self, m):
        s = mod(m, self.d, self.n)

        print(f"Original S = {s}")
        return s


if __name__ == "__main__":
    parameters = [[11, 3, 5]]  # p, q, m

    for n, (p, q, m) in enumerate(parameters):
        print("=" * 20)
        print("No.{} (p={}, q={}, M={})\n".format(n + 1, p, q, m))
        blind = Blind(p, q)
        blind_m = blind.blinding(m)
        blind_s = blind.signing(blind_m)
        s = blind.unblinding(blind_s)
        original_s = blind.original(m)
        print("=" * 20, end="\n\n")
