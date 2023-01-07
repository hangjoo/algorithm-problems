import sys


input = sys.stdin.readline


def solution():
    n = int(input())
    factorial_num = get_factorial(n)

    for idx, char in enumerate(reversed(str(factorial_num))):
        if char != "0":
            print(idx)
            break


def get_factorial(num: int) -> int:
    factorial_num = 1
    for i in range(2, num + 1):
        factorial_num *= i

    return factorial_num


if __name__ == "__main__":
    solution()
