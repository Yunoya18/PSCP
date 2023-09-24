"""Sequence VII"""
def main():
    """process"""
    num = int(input())
    end = num + 1
    for i in reversed(range(num)):
        for j in range(1, end - i):
            print(j, end=" ")
        print()
    for mmm in range(num - 1):
        for nnn in range(1, end - mmm - 1):
            print(nnn, end=" ")
        print()

main()
