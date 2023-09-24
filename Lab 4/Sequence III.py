"""Sequence III"""
def main():
    """process"""
    num = int(input())
    start = 2
    end = num + 2
    for _ in range(num):
        for j in range(start, end):
            print(j, end=" ")
        print()
        start += 1
        end += 1

main()
