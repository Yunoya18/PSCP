"""Left Arrow"""
def main():
    """process"""
    width = int(input())
    height = int(input())
    space = height // 2
    for _ in range(height // 2):
        for _ in range(space):
            print(" ", end="")
        for _ in range(width):
            print("*", end="")
        space -= 1
        print()
    for _ in range(width):
        print("*", end="")
    print()
    for _ in range(height // 2):
        space += 1
        for _ in range(space):
            print(" ", end="")
        for _ in range(width):
            print("*", end="")
        print()

main()
