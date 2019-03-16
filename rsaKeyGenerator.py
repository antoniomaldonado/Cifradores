import math
import random
import utils.primeNumber as primeNumber


def generate_asym_key(key_size):
    p = 0
    q = 0
    while p == q:
        p = primeNumber.generate_prime(key_size)
        q = primeNumber.generate_prime(key_size)
    n = p * q
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    d = primeNumber.find_inverse(e, (p - 1) * (q - 1))

    return (n, e), (n, d)


def save_keys_to_files(name, key_size):
    pub_key, priv_key = generate_asym_key(key_size)
    save_key_to_file(key_size, name, pub_key, 'pub')
    save_key_to_file(key_size, name, priv_key, 'priv')


def save_key_to_file(key_size, name, key, key_type):
    print('Saving %s %s key in %s_%s.txt...' %
          (name, key_type, name, key_type))
    fo = open('%s_%s.txt' % (name, key_type), 'w')
    fo.write('%s,%s,%s' % (key_size, key[0], key[1]))
    fo.close()


def main():
    print('1. Introduce a name:')
    key_name = input()
    print('Generating keys...')
    save_keys_to_files(key_name, 1024)
    print('Asymmetric keys generation successful.')


if __name__ == '__main__':
    main()
