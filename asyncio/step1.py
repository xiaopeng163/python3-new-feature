def search(n):
    a,b = 0, 1
    while True:
        if len(str(a)) >= n:
            return a
        a, b = b, a + b


if __name__ == "__main__":
    print(search(30))
    print(search(40))
