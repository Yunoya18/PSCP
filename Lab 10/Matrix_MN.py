"""Matrix_MN"""
def main():
    """process"""
    num_list = []
    row = int(input())
    col = int(input())
    for _ in range(row):
        num = []
        for _ in range(col):
            num.append(int(input()))
        num_list.append(num)
    for i in num_list:
        print(*i)

main()
