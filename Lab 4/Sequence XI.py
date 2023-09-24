"""Sequence XI"""
def upper(num):
    """print upper"""
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            if col >= row+1:
                print("%02d " % row, end="")
            else:
                print("%02d " % col, end="")
        for another_col in reversed(range(1, num)):
            if another_col >= row+1:
                print("%02d " % row, end="")
            else:
                print("%02d " % another_col, end="")
        print()

def lower(num):
    """print lower"""
    for row in reversed(range(1, num)):
        for col in range(1, num + 1):
            if col >= row:
                print("%02d " % row, end="")
            else:
                print("%02d " % col, end="")
        for another_col in reversed(range(1, num)):
            if another_col >= row:
                print("%02d " % row, end="")
            else:
                print("%02d " % another_col, end="")
        print()

def main():
    """process"""
    num = int(input())
    upper(num)
    lower(num)

main()
