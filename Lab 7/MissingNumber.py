"""MissingNumber"""
def main():
    """process"""
    num = int(input())
    total_set = set()
    check_set = set()
    for i in range(1, num+1):
        total_set.add(i)
    while True:
        check = int(input())
        if check == 0:
            break
        else:
            check_set.add(check)
    print(*sorted(total_set-check_set), sep="\n")

main()
