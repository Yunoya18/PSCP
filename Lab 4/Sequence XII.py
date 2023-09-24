"""Sequence XII"""
def upper(num):
    """upper part"""
    for row in range(1, num + 1): #Q1, Q2
        for col in range(1, num + 1):
            if row <= col:
                print("%02d " % (num + row - col), end="")
            else:
                print("%02d " % (num - row + col), end="")
        for another_col in reversed(range(1, num)):
            if another_col >= row:
                print("%02d " % (num + row - another_col), end="")
            else:
                print("%02d " % (num - row + another_col), end="")
        print()

def lower(num):
    """lower part"""
    for row in range(1, num):
        for col in reversed(range(1, num + 1)):
            if row <= col - 1:
                print("%02d " % (num + row - col + 1), end="")
            else:
                print("%02d " % (num - row + col - 1), end="")
        for another_col in range(1, num):
            if row <= another_col:
                print("%02d " % (num + row - another_col), end="")
            else:
                print("%02d " % (num - row + another_col), end="")
        print()

def main():
    """process"""
    num = int(input())
    upper(num)
    lower(num)

main()
