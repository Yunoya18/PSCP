"""Sequence IV"""
def main():
    """process"""
    num = int(input())
    start = 1
    end = num + 1
    for _ in range(num):
        for j in range(start, end):
            print(j, end=" ")
        start += num
        end += num
        print()

main()
