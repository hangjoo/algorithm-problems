BRACKET_MATCH = {
    ")": "(",
    "]": "[",
}


def solution():
    sents = []
    while True:
        sent = input()
        if sent == ".":
            break
        sents.append(sent)

    for sent in sents:
        is_balanced = True
        bracket_stack = []
        for char in sent:
            if char in tuple(BRACKET_MATCH.values()):
                bracket_stack.append(char)
            elif char in tuple(BRACKET_MATCH.keys()):
                try:
                    last_bracket = bracket_stack.pop()
                    if last_bracket != BRACKET_MATCH[char]:
                        is_balanced = False
                        break
                except IndexError:
                    is_balanced = False
                    break
            else:
                continue

        if bracket_stack or not is_balanced:
            print("no")
        else:
            print("yes")


if __name__ == "__main__":
    solution()
