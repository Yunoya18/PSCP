"""SqFree"""
def main():
    """process"""
    num = int(input())
    count = 0
    check = 0
    for i in range(1, num+1):
        for num in range(2, int(i ** 0.5) + 1):
            if i % (num**2) == 0:
                check += 1
        if check == 0:
            count += 1
        check = 0
    print(count)

main()
