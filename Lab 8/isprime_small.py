"""isprime_small"""
def main():
    """process"""
    num = int(input())
    check = 0
    if num == 1:
        print("No")
    else:
        for i in range(2, num):
            if num % i == 0:
                check += 1
        if check == 0:
            print("Yes")
        else:
            print("No")

main()
