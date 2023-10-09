"""Olympic"""
def main():
    """process"""
    info = {}
    num = int(input())
    for _ in range(num):
        text = input().split()
        info[text[0]] = tuple(map(int, text[1:]))
    info = dict(sorted(info.items(), key=lambda x: x[0]))
    info = dict(sorted(info.items(), key=lambda x: x[1], reverse=True))
    check = ""
    check_num = 0
    num_iter = iter(list(range(1, num + 1)))
    for key, value in info.items():
        step_num = next(num_iter)
        score = " ".join(map(str, value))
        if value == check:
            print(check_num, key, score, sum(value))
        else:
            print(step_num, key, score, sum(value))
            check_num = step_num
        check = value

main()
