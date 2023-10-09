"""Diamond I"""
def main():
    """calculate"""
    row = int(input())
    col = int(input())
    num_list = []
    total = 0
    for _ in range(row):
        num = input()
        num_list.append(num.split())
    for i in range(col):
        check = 0
        for j in range(row):
            check += int(num_list[j][i])
        if check > total:
            total = check
    print(total)

main()
