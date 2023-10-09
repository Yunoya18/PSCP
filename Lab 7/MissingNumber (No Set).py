"""MissingNumber (No Set)"""
def main():
    """process"""
    num = int(input())
    check_list = []
    while True:
        check = int(input())
        if check == 0:
            break
        else:
            check_list.append(check)
    for i in range(1, num + 1):
        if i not in check_list:
            print(i)

main()
