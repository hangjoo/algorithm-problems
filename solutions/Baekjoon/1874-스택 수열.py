def solution():
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    nums = list(range(n, 0, -1))

    is_available = True
    operations = []

    stack = []
    while nums:
        if not stack:
            stack.append(nums.pop())
            operations.append("+")
        else:
            if stack[-1] == seq[0]:
                stack.pop()
                seq.pop(0)
                operations.append("-")
            else:
                stack.append(nums.pop())
                operations.append("+")

    for seq_item, stack_item in zip(seq, reversed(stack)):
        if seq_item == stack_item:
            operations.append("-")
        else:
            is_available = False

    if not is_available:
        print("NO")
    else:
        print("\n".join(operations))


if __name__ == "__main__":
    solution()
