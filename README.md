# Information-Security
KAIST CS448 Introduction to Information Security(정보보호개론) 기말고사 대비로 구현한 프로그램 입니다. 암호에서는 큰 수를 많이 사용하기 떄문에 가장 효율적인 알고리즘을 사용하여 구현하였습니다. DES, AES, SHA-3, ECDSA 와 같은 오픈소스로 많이 풀려있는 암호는 따로 구현하지 않았고, 과제로 제출한 프로그램을 그대로 사용하였기 떄문에 첨부하지 않았습니다(마찬가지로 과제 소스코드도 첨부하지 않았습니다).

## Usage
`$ python3 main.py`
`$ python3 <filename>`

## Contents
1. utils.py
    - exeu : 확장 유클리드 알고리즘
    - mod : 매우 큰 수에서도 O(log n)로 작동하는 모듈러
    - gcd : 최대공배수
    - get_order : totient function
    - is_prime : 최적화 된 소수 찾는 알고리즘
    - get_coprime : 서로소 찾는 알고리즘
    - get_generatives : generator g 리스트 반환
    - is_primitive : primitive 인지 확인
2. classic.py
    - Caesar
    - Affine
    - Vigenere
3. rsa.py : RSA 암호
4. elgamal.py
    - ElGamal 암호 
    - Elgamal 전자서명
5. blind.py : blind signature 
6. ecdh.py : Elliptic Curve Diffie Hellman
7. ds : Digital Signature
    - rsa_signing : RSA 서명
    - dh : 디피헬만
7. fiat : fiat-shamir heuristic