from utils import get_orders, mod, gcd


def find_period(a, x, n):
    start = mod(a, x, n)

    for r in range(1, 100):
        temp = mod(a, x + r, n)
        if start == temp:
            # print(f"{a} ^ {x} = {a}  ^ {x + r}")
            return r


factors = get_orders(77)
print(factors)
for a in factors:
    r = find_period(a, 1, 77)
    if r % 2 == 1:
        continue

    temp = mod(a, r / 2, 77)
    if temp == (-1 % 77):
        continue

    print(f"a = {a}, r = {r}")
    x = gcd(a ** (r / 2) + 1, 77)
    y = gcd(a ** (r / 2) - 1, 77)

    print(x, y)
