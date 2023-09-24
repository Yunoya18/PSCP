"""Sequence N"""
def main():
    """process"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if j == 0:
                print("*", end="")
            elif j == num - 1:
                print("*", end="")
            elif j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()
