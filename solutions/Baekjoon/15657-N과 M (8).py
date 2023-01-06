import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def solution():
    _, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    sequences = combinations_with_replacement(nums, m)
    for seq in sequences:
        print(" ".join(map(str, seq)))


if __name__ == "__main__":
    solution()
