def solution():
    word = input()
    counts = []
    for ord_index in range(ord("a"), ord("z") + 1):
        alphabet = chr(ord_index)
        counts.append(str(word.find(alphabet)))

    print(" ".join(counts))


if __name__ == "__main__":
    solution()
