import sys


input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    password_of_email = {}
    for _ in range(n):
        email, password = input().split()
        password_of_email[email] = password

    for _ in range(m):
        email = input().strip()
        print(password_of_email[email])


if __name__ == "__main__":
    solution()
