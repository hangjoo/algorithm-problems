from collections import Counter
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    sorted_nums = sorted(nums)
    count_nums = Counter(nums)

    # average
    print(round(sum(nums) / n))

    # median
    print(sorted_nums[n // 2])

    # mode
    count_pairs = count_nums.most_common()
    maximum = count_pairs[0][1]
    maximum_nums = []
    for num, count in count_pairs:
        if count == maximum:
            maximum_nums.append(num)
    maximum_nums = sorted(maximum_nums)
    if len(maximum_nums) >= 2:
        print(maximum_nums[1])
    else:
        print(maximum_nums[0])

    # range
    print(sorted_nums[-1] - sorted_nums[0])


if __name__ == "__main__":
    solution()
