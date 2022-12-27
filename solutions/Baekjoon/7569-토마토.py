import sys


input = sys.stdin.readline


DIRECTIONS = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1,),
]


def solution():
    m, n, h = map(int, input().split())

    current_ripe = []
    tomato_map = []
    for h_i in range(h):
        tomato_floor = []
        for n_i in range(n):
            row = list(map(int, input().split()))
            tomato_floor.append(row)
            for m_i in range(m):
                if row[m_i] == 1:
                    current_ripe.append((h_i, n_i, m_i))
        tomato_map.append(tomato_floor)

    days = 0
    while True:
        next_ripe_tomato = []
        for tomato_pos in current_ripe:
            cur_h, cur_n, cur_m = tomato_pos
            for move_h, move_n, move_m in DIRECTIONS:
                move_h += cur_h
                move_n += cur_n
                move_m += cur_m

                if all((0 <= move_h < h, 0 <= move_n < n, 0 <= move_m < m)):
                    if tomato_map[move_h][move_n][move_m] == 0:
                        tomato_map[move_h][move_n][move_m] = 1
                        next_ripe_tomato.append((move_h, move_n, move_m))

        if next_ripe_tomato:
            current_ripe = next_ripe_tomato
            days += 1
        else:
            break

    for tomato_floor in tomato_map:
        for tomato_row in tomato_floor:
            if 0 in tomato_row:
                print(-1)
                return
    print(days)


if __name__ == "__main__":
    solution()
