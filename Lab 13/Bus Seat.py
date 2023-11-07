"""Bus Seat"""
def main():
    """process"""
    row = int(input())
    col = int(input())
    check = int(input())
    for i in reversed(range(1, row + 1)):
        if i % 2 == 0 and i != row:
            print()
        for j in range(col):
            current = i + (j*row)
            if current == check:
                print("XX", end=" ")
            else:
                print("%02d" % current, end=" ")
        print()

main()
