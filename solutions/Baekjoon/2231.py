def solution():
    n = int(input())
    for num in range(1, n):
        nums_array = [num]
        nums_array += list(map(int, list(str(num))))
        if sum(nums_array) == n:
            print(num)
            return

    print(0)


if __name__ == "__main__":
    solution()
