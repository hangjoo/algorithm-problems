def solution():
    n = int(input())

    base = 1
    level = 0
    while True:
        base += 6 * level
        if n <= base:
            print(level + 1)
            return

        level += 1


if __name__ == "__main__":
    solution()
