def solution():
    while True:
        lengths = map(int, input().split())
        a, b, c = sorted(lengths)

        if a == b == c == 0:
            return

        if (a ** 2) + (b ** 2) == (c ** 2):
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solution()
