"""Cha Cha Cha"""
import math
def main():
    """process"""
    day = int(input())
    total = 0
    for _ in range(day):
        hour = float(input())
        total += math.ceil(hour)
    print(total * 8720)

main()
