def solution():
    a, b = input().split()

    a = int(a[::-1])
    b = int(b[::-1])

    print(max(a, b))


if __name__ == "__main__":
    solution()
