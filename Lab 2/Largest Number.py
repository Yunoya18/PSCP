"""Largest Number"""
def main():
    """process"""
    num1 = input()
    num2 = input()
    num3 = input()
    num = int(num1 + num2 + num3)
    if num < int(num1 + num3 + num2):
        num = int(num1 + num3 + num2)
    if num < int(num2 + num1 + num3):
        num = int(num2 + num1 + num3)
    if num < int(num2 + num3 + num1):
        num = int(num2 + num3 + num1)
    if num < int(num3 + num1 + num2):
        num = int(num3 + num1 + num2)
    if num < int(num3 + num2 + num1):
        num = int(num3 + num2 + num1)
    print(num)

main()
