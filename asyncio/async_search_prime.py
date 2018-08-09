from math import sqrt

def async_search_prime():
    a, b = 0, 1
    while True:
        result = yield from is_prime(a)
        if result:
            print(f'found: {a}')
        a, b = b, a + b


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield
    return True


if __name__ == "__main__":
    pass