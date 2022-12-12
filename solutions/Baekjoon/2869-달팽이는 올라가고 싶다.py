from math import ceil


def solution():
    a, b, v = map(int, input().split())

    if a == v:
        print("1")
    else:
        day = ceil((v - a) / (a - b)) + 1
        print(day)


if __name__ == "__main__":
    solution()
