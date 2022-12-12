import sys


input = sys.stdin.readline


def solution():
    n = int(input())

    nums = []
    for _ in range(n):
        nums.append(int(input()))

    sorted_nums = sorted(nums)
    for num in sorted_nums:
        print(num)


if __name__ == "__main__":
    solution()
