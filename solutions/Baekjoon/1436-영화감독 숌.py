def solution():
    n = int(input())
    n_count = 0

    num = 0
    while n_count < n:
        num += 1
        num_str = str(num)
        if num_str.find("666") != -1:
            n_count += 1

    print(num)


if __name__ == "__main__":
    solution()
