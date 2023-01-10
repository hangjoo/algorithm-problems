from collections import defaultdict
import sys


input = sys.stdin.readline


def solution():
    tc = int(input())
    for _ in range(tc):
        n = int(input())

        cloth_counts = defaultdict(int)
        for _ in range(n):
            _, cloth_type = input().split()
            cloth_counts[cloth_type] += 1

        answer = 1
        for cloth_count in cloth_counts.values():
            answer *= cloth_count + 1

        print(answer - 1)


if __name__ == "__main__":
    solution()
