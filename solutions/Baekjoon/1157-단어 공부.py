from collections import Counter


def solution():
    word = input().lower()
    chr_counter = Counter(word)
    chr_nums = chr_counter.most_common()

    if len(chr_nums) == 1:
        print(chr_nums[0][0].upper())
    elif chr_nums[0][1] > chr_nums[1][1]:
        print(chr_nums[0][0].upper())
    else:
        print("?")


if __name__ == "__main__":
    solution()
