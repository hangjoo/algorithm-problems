import sys


input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    connect = {node: set() for node in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        connect[u].add(v)
        connect[v].add(u)

    component_num = 0
    is_visit = {node: False for node in range(1, n + 1)}
    for node in range(1, n + 1):
        if is_visit[node]:
            continue

        is_visit[node] = True
        component_num += 1

        queue = [node]
        while queue:
            cur_node = queue.pop(0)
            for connect_node in connect[cur_node]:
                if not is_visit[connect_node]:
                    queue.append(connect_node)
                    is_visit[connect_node] = True

    print(component_num)


if __name__ == "__main__":
    solution()
