def solution():
    n = int(input())
    man_info = [tuple(map(int, input().split())) for _ in range(n)]

    rank = []
    for i, (i_weight, i_height) in enumerate(man_info):
        current_rank = 1
        for j, (j_weight, j_height) in enumerate(man_info):
            if i == j:
                continue

            if j_weight > i_weight and j_height > i_height:
                current_rank += 1

        rank.append(str(current_rank))

    print(" ".join(rank))


if __name__ == "__main__":
    solution()
