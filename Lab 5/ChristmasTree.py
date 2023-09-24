"""ChristmasTree"""
def main():
    """process"""
    size = int(input())
    num = int(input())
    for i in range(1, size+1):
        print(" " * (size - i), end="")
        for _ in range(i*2 - 1):
            print("*", end="")
        print()
    for i in range(num):
        print(" " * ((size*2 - 1)//2 - 1), end="")
        print("---")

main()
