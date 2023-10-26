"""All_Primes"""
def main():
    """process"""
    num = int(input())
    count = 0
    check = 0
    for i in range(1, num + 1):
        if i != 1:
            for j in range(2, i):
                if i % j == 0:
                    check += 1
            if check == 0:
                count += 1
            check = 0
    print(count)

main()
