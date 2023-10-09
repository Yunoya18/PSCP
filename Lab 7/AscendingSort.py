"""AscendingSort"""
def main():
    """process"""
    num_list = []
    for _ in range(5):
        num = int(input())
        num_list.append(num)
    num_list.sort()
    for i in num_list:
        print(i)

main()
