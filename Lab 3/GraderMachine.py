"""GraderMachine"""
def main():
    """calculate"""
    start = int(input())
    end = int(input())
    total = 0
    print("pass :", end=" ")
    if end >= start:
        for i in range(start, end+1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    elif start > end:
        for i in range(start, end-1, -1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    print()
    print("Sum : " + str(total))

main()
