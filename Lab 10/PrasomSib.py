"""PrasomSib"""
def main():
    """process"""
    num = input()
    count = 0
    while len(num) > 0:
        check = 0
        for i in num:
            check += int(i)
            if check == 10:
                count += 1
                break
        num = num[1:]
    print(count)

main()
