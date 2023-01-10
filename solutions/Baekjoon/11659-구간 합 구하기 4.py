import sys
from typing import List

input = sys.stdin.readline


def solution():
    _, m = map(int, input().split())
    nums = list(map(int, input().split()))
    sums = convert_to_sum(nums)

    for _ in range(m):
        s_i, e_i = map(int, input().split())
        print(sums[e_i] - sums[s_i - 1])


def convert_to_sum(nums: List[int]) -> List[int]:
    sums = [0] * (len(nums) + 1)

    for idx, num in enumerate(nums, 1):
        sums[idx] = sums[idx - 1] + num

    return sums


if __name__ == "__main__":
    solution()
