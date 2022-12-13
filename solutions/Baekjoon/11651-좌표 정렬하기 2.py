def solution():
    n = int(input())
    coor = [tuple(map(int, input().split())) for _ in range(n)]

    sorted_coor = sorted(coor, key=lambda x: (x[1], x[0]))
    for x, y in sorted_coor:
        print(x, y)


if __name__ == "__main__":
    solution()
