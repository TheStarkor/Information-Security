from utils import mod, exeu, get_coprime


def rsa_signing(p, q, m):
    n = p * q
    pi = (p - 1) * (q - 1)
    e = get_coprime(pi)
    d = exeu(e, pi)
    s = mod(m, d, n)
    v = mod(s, e, n)

    print(f"{m} ?= {v}(s = {s})")


def dh(p, g, x_a, x_b):
    y_a = mod(g, x_a, p)
    y_b = mod(g, x_b, p)

    k_a = mod(y_b, x_a, p)
    k_b = mod(y_a, x_b, p)

    print(f"(Ya, Yb) = {y_a, y_b}, (Ka, Kb) = {k_a, k_b}")


if __name__ == "__main__":
    # rsa_signing(2357, 2551, 1234)  # p, q, m
    p, g = 101, 2
    dh(p, g, 3, 7)
