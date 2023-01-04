import sys
from typing import List, Tuple


input = sys.stdin.readline


def solution():
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]

    white_num, blue_num = divide_and_conquer(paper, 0, n, 0, n)

    print(white_num, blue_num, sep="\n")


def divide_and_conquer(paper: List[List[int]], h_s: int, h_e: int, w_s: int, w_e: int) -> Tuple[int]:
    is_available = check(paper, h_s, h_e, w_s, w_e)
    if is_available == 0:
        return 1, 0
    elif is_available == 1:
        return 0, 1
    else:
        h_m = (h_s + h_e) // 2
        w_m = (w_s + w_e) // 2
        blue_1, white_1 = divide_and_conquer(paper, h_s, h_m, w_s, w_m)
        blue_2, white_2 = divide_and_conquer(paper, h_s, h_m, w_m, w_e)
        blue_3, white_3 = divide_and_conquer(paper, h_m, h_e, w_s, w_m)
        blue_4, white_4 = divide_and_conquer(paper, h_m, h_e, w_m, w_e)

        blue_num = blue_1 + blue_2 + blue_3 + blue_4
        white_num = white_1 + white_2 + white_3 + white_4

        return blue_num, white_num


def check(paper: List[List[int]], h_s: int, h_e: int, w_s: int, w_e: int,) -> int:
    first_item = paper[h_s][w_s]
    for row in paper[h_s:h_e]:
        for item in row[w_s:w_e]:
            if item != first_item:
                return -1

    return first_item


if __name__ == "__main__":
    solution()
