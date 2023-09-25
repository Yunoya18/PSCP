"""Meteorite"""
def main():
    """calculate"""
    weight = float(input())
    split = int(input())
    check = float(input())
    total = 0
    count = 1
    while True:
        if weight < check:
            break
        else:
            total += count
            weight /= split
            count *= split
    print(total)

main()
