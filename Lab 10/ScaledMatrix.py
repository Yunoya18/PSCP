"""ScaledMatrix"""
def main():
    """process"""
    row = int(input())
    col = int(input())
    num_list = []
    check_num = []
    for _ in range(row):
        num = []
        for _ in range(col):
            num_input = float(input())
            check_num.append(num_input)
            num.append(num_input)
        num_list.append(num)
    check_num.sort()
    for i in range(row):
        for j in range(col):
            print("%.2f" % ((num_list[i][j]-check_num[0])/(check_num[-1]-check_num[0])), end=" ")
        print()

main()
