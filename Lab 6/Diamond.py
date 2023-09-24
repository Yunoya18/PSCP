"""Diamond"""
def main():
    """process"""
    num = int(input())
    for i in range(num//2 + 1):
        for j in range(num):
            if i == (num//2):
                print("*", end="")
            elif j == (num//2 + i):
                print("*", end="")
            elif j == (num//2 - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for mmm in range(1, num//2 + 1):
        for nnn in range(num):
            if nnn == mmm:
                print("*", end="")
            elif nnn == (num - mmm - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()
