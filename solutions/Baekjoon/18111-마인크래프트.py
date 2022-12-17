from collections import Counter
import sys

input = sys.stdin.readline


def solution():
    n, m, b = map(int, input().split())
    block_map = []
    for _ in range(n):
        block_map.extend(map(int, input().split()))
    block_height_counter = Counter(block_map)

    answer_height = float("inf")
    answer_time = float("inf")
    for goal_height in range(min(block_map), 257):
        add_blocks, sub_blocks = 0, 0
        for block_height, count in block_height_counter.items():
            if block_height >= goal_height:
                sub_blocks += (block_height - goal_height) * count
            else:
                add_blocks += (goal_height - block_height) * count

        if add_blocks <= sub_blocks + b:
            if add_blocks + (2 * sub_blocks) <= answer_time:
                answer_height = goal_height
                answer_time = add_blocks + (2 * sub_blocks)

    print(answer_time, answer_height)


if __name__ == "__main__":
    solution()
