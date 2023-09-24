"""Sequence V"""
def main():
    """process"""
    num = int(input())
    count = 0
    for i in reversed(range(1, num + 1)):
        print(i, end=" ")
        count += 1
        if count % 7 == 0:
            print()

main()
