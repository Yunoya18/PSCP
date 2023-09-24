"""Sequence VIII"""
def main():
    """process"""
    num = int(input())
    end = num + 1
    for i in reversed(range(num)):
        print("   " * i, end="")
        for j in range(1, end - i):
            print("%02d" % j, end=" ")
        print()

main()
