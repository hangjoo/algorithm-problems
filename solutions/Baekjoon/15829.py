R = 31
M = 1234567891


def char_to_num(char: str):
    return ord(char) - ord("a") + 1


def solution():
    _ = int(input())
    sentence = input()

    h = 0
    for i, char in enumerate(sentence):
        h += char_to_num(char) * (R ** i)
    h = h % M

    print(h)


if __name__ == "__main__":
    solution()
