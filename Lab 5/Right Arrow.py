"""Right Arrow"""
def main():
    """process"""
    width = int(input())
    height = int(input())
    for i in range(height//2 + 1):
        print(" " * i, end="")
        print("*" * width)
    for j in reversed(range(height//2)):
        print(" " * j, end="")
        print("*" * width)

main()
