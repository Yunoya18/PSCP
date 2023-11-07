"""HW_DotE"""
import math
def main():
    """calculate"""
    num = int(input())
    total = math.factorial(num)/(math.factorial(num // 2)*math.factorial(num - (num//2)))\
        * (1 if num % 2 == 0 else 2)
    total = int(total)
    print(total)

main()
