import sys


input = sys.stdin.readline

ALL_SET = int("0b{}".format("1" * 20), 2)
EMPTY_SET = int("0b{}".format("0" * 20), 2)


def solution():
    m = int(input())

    cur_set = EMPTY_SET
    for _ in range(m):
        args = input().split()
        cur_set = task(args, cur_set)


def task(args: list[str], cur_set: int):
    operation = args[0]

    if operation in ("add", "remove", "check", "toggle"):
        x = int(args[1])
        bit = get_bit_from_position(x)
        if operation == "add":
            cur_set = cur_set | bit

        elif operation == "remove":
            cur_set = cur_set & ~bit

        elif operation == "check":
            if cur_set & bit:
                print("1")
            else:
                print("0")

        elif operation == "toggle":
            cur_set = cur_set ^ bit
    else:
        if operation == "all":
            cur_set = ALL_SET

        elif operation == "empty":
            cur_set = EMPTY_SET

    return cur_set


def get_bit_from_position(bit_position: int) -> int:
    bit = 1 << (bit_position - 1)

    return bit


if __name__ == "__main__":
    solution()
