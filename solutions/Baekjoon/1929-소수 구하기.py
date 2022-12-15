def solution():
    m, n = map(int, input().split())

    check_prime = {num: True for num in range(1, n + 1)}
    check_prime[1] = False

    check_max = int(n ** 0.5)
    for num in range(2, check_max + 1):
        if check_prime[num]:
            for effect_num in range(num * 2, n + 1, num):
                check_prime[effect_num] = False

    for num in range(m, n + 1):
        if check_prime[num]:
            print(num)


if __name__ == "__main__":
    solution()
