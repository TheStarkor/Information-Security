from utils import (
    exeu,
    mod,
    gcd,
    get_order,
    is_prime,
    get_coprime,
    get_generatives,
    is_primitive,
    intstr_to_list,
    list_to_intstr,
    str_to_list,
    list_to_str,
)
from rsa import RSA
from elgamal import ElgamalEncryption, ElgamalSignature
from blind import Blind
from ecdh import ECDH
from ds import rsa_signing, dh
from classic import Caesar, Affine, Vigenere
from fiat import Fiat

##################################################################################

# print(exeu(a, p))  # a^(-1) mod p
# print(mod(a, b, p))  # a^b % c fast modular
# print(gcd(a, b))
# print(get_order(n))  # totient function or order
# print(is_prime(n))
# print(get_coprime(pi))  # gcd(n, pi) = 1
# print(get_generatives(101))  # find primitive numbers until p-1
a = get_generatives(101)
print(a)
print(len(a))
# print(is_primitive(a, p))
# print(intstr_to_list("1234")) # "1234" -> [1, 2, 3, 4]
# print(list_to_intstr([1, 2, 3, 4])) # [1, 2, 3, 4] -> "1234"
# print(str_to_list("abcd")) # "abcd" -> [0, 1, 2, 3]
# print(list_to_str([0, 1, 2, 3])) # [0, 1, 2, 3] -> "abcd"

##################################################################################

# #### RSA encryption
# parameters = [[2357, 2551, 1234], [885320963, 238855417, 1234567]]  # p, g, m

# for n, (p, q, m) in enumerate(parameters):
#     print("=" * 20)
#     print("No.{} (p={}, q={}, M={})\n".format(n + 1, p, q, m))
#     rsa = RSA(p, q, m)
#     print("C =", rsa.encryption(rsa.e), end="\n\n")
#     print("M =", rsa.decryption(rsa.d))
#     print("=" * 20, end="\n\n")


# #### Elgamal encryption
# parameters = [[23, 7, 9, 20, 3]]  # p, g, x, m, k

# for n, (p, g, x, m, k) in enumerate(parameters):
#     print("=" * 20)
#     print(f"No.{n+1} (p={p}, q={q}, x={x}, M={m}, k={k}")
#     elgamalencryption = ElgamalEncryption(p, g, x)
#     c1, c2 = elgamalencryption.encrypt(m, k)
#     m = elgamalencryption.decrypt(c1, c2)
#     print("=" * 20, end="\n\n")

# #### Blind Signature
# parameters = [[11, 3, 5]]  # p, q, m

# for n, (p, q, m) in enumerate(parameters):
#     print("=" * 20)
#     print("No.{} (p={}, q={}, M={})\n".format(n + 1, p, q, m))
#     blind = Blind(p, q)
#     blind_m = blind.blinding(m)
#     blind_s = blind.signing(blind_m)
#     s = blind.unblinding(blind_s)
#     original_s = blind.original(m)
#     print("=" * 20, end="\n\n")

# #### Elgamal Signature
# parameters = [[23, 10, 9, 1234, 3]]  # p, g, x, m, k

# for n, (p, g, x, m, k) in enumerate(parameters):
#     print("=" * 20)
#     print(f"No.{n+1} (p={p}, q={q}, x={x}, M={m}, k={k}")
#     elgamalsignature = ElgamalSignature(p, g, x)
#     r, s = elgamalsignature.generate(m, k)
#     elgamalsignature.verify(m, r, s)
#     print("=" * 20, end="\n\n")

# #### ECDH
# p, a, b, g_x, g_y, n = 17, 2, 2, 5, 1, 19
# alpha, beta = 3, 9
# ecdh = ECDH(p, a, b, g_x, g_y, n)  # p, a, b, g_x, g_y, n
# b_x, b_y = ecdh.encrypt(beta)
# a_x, a_y = ecdh.encrypt(alpha)
# print(f"Bob: {b_x, b_y}, Alice: {a_x, a_y}")
# b = ecdh.verify(beta, a_x, a_y)
# a = ecdh.verify(alpha, b_x, b_y)
# print(f"Bob: {b[0], b[1]}, Alice: {a[0], a[1]}")

# #### Fiat-Shamir
# r, s, n = 16, 12, 77
# fiat = Fiat(r, s, n)
# fiat.first(1) # Select 0 or 1
# fiat.verify()

##################################################################################

##### RSA Signing
# rsa_signing(2357, 2551, 1234)  # p, q, m

##### DSA

##### KCDSA

##### Schnorr Signature Scheme

##### DH
# dh(23, 5, 6, 15)  # p, g, x_a, x_b

##################################################################################

# #### Caesar
# k = 12
# m = str_to_list("abcde")

# caesar = Caesar(k)
# c = caesar.encrypt(m)
# m = caesar.decypt(c)
# print(f"C = {list_to_str(c)}, M = {list_to_str(m)}")

# #### Affine
# c = str_to_list("wegvrjepqnwezbdzqetgzbigvpta")
# k1 = exeu(5, 26)
# k2 = 13
# affine = Affine(k1, k2)
# res = affine.decrypt(c)
# print(f"M = {list_to_str(res)}")

# #### Vigenere
# key = intstr_to_list("20170317")
# vigenere = Vigenere(key, 10)
# m = intstr_to_list("314159265358979323846264")
# res = vigenere.encrypt(m)
# print(f"C = {list_to_intstr(res)}")

##################################################################################
