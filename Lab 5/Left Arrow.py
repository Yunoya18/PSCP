"""Left Arrow"""
def main():
    """process"""
    width = int(input())
    height = int(input())
    for i in range(height // 2 + 1):
        print(" " * (height // 2 - i), end="")
        print("*" * width)
    for j in range(height // 2):
        print(" " * (j + 1), end="")
        print("*" * width)

main()
