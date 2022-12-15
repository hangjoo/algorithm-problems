def solution():
    t = int(input())

    for _ in range(t):
        _, m = map(int, input().split())
        docs = list(map(int, input().split()))

        print_num = 0
        while True:
            cur_doc = docs.pop(0)

            if not docs or cur_doc >= max(docs):
                print_num += 1
                if m == 0:
                    print(print_num)
                    break
                else:
                    m -= 1
            else:
                if m == 0:
                    m = len(docs)
                else:
                    m -= 1
                docs.append(cur_doc)


if __name__ == "__main__":
    solution()
