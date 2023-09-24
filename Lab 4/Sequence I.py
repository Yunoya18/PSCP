"""Sequence I"""
def main():
    """process"""
    num = int(input())
    for _ in range(num):
        for j in range(1, num + 1):
            print(j, end=" ")
        print()

main()
