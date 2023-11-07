"""isPrime_large"""
def main():
    """process"""
    num = int(input())
    check = 0
    if num == 1:
        print("NO")
    elif num == 2:
        print("YES")
    elif num % 2 == 0:
        print("NO")
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                check += 1
        if check == 0:
            print("YES")
        else:
            print("NO")

main()
