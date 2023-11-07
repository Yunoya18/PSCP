"""Mastermind"""
def main():
    """process"""
    ans = input()
    check = input()
    ans_b = 0
    ans_w = 0
    ans_list = list(ans)
    for i in range(4):
        if check[i] == ans[i]:
            ans_b += 1
    for j in check:
        if j in ans_list:
            ans_w += 1
            ans_list.remove(j)
    ans_w -= ans_b
    print(("B" * ans_b) + ("W" * ans_w) + ("O" * (4-ans_b-ans_w)))

main()
