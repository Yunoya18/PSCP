"""Sequence IX"""
def main():
    """process"""
    num = int(input())
    end = num + 1
    for i in reversed(range(num)):
        print("   " * i, end="")
        for j in range(1, end - i):
            print("%02d" % j, end=" ")
        for mmm in reversed(range(1, end - i - 1)):
            print("%02d" % mmm, end=" ")
        print()

main()
