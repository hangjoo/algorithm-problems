def solution():
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        people_num = [[0 for _ in range(n)] for _ in range(k + 1)]

        for i in range(n):
            people_num[0][i] = i + 1

        for k_i in range(1, k + 1):
            for n_i in range(n):
                people_num[k_i][n_i] = sum(people_num[k_i - 1][:n_i + 1])

        print(people_num[-1][-1])


if __name__ == "__main__":
    solution()
