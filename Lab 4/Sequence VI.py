"""Sequence VI"""
def main():
    """process"""
    num = int(input())
    end = num + 1
    for i in reversed(range(num)):
        for j in range(1, end - i):
            print(j, end=" ")
        print()

main()
