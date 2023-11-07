"""isPrime (LARGER)"""
def main():
    """process"""
    num = int(input())
    check = 0
    if num == 1:
        print("False")
    elif num == 2:
        print("True")
    elif num % 2 == 0:
        print("False")
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                check += 1
        if check == 0:
            print("True")
        else:
            print("False")

main()
