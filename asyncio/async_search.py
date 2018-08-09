def async_search(n):
    a, b = 0, 1
    while True:
        if longer(a, n):
            return a
        yield
        a, b = b, a + b

def longer(x, n):
    if len(str(x)) >= n:
        return True
    return False


if __name__ == "__main__":
    iterator1 = async_search(5)
