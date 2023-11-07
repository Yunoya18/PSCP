"""SuperMarketV2"""
def main():
    """calculate"""
    num = int(input())
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    item_lst = [int(input()) for _ in range(num)]
    item_lst.sort()
    check1 = sum(item_lst) * ((100-num_b)/100 if sum(item_lst) >= num_a else 1) # only pro 1
    check2 = sum(item_lst[:-1]) + item_lst[-1] * ((100-num_c)/100) # only pro 2
    check3 = sum(item_lst)
    for i in item_lst:
        check_item = item_lst.copy()
        check_item.remove(i)
        check = sum(check_item) + (i * ((100-num_c)/100))
        if check >= num_a:
            check3 = check * ((100-num_b)/100)
    print(int(min(check1, check2, check3)))

main()
