"""Kangaroo"""
def main():
    """process"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(max(num2 - num1, num3 - num2) - 1)

main()
