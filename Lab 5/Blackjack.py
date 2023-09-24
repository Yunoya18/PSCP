"""Blackjack"""
def main():
    """calculate"""
    num = int(input())
    total = 0
    count = 0
    for _ in range(num):
        check = input()
        if check == "J" or check == "Q" or check == "K":
            total += 10
        elif check == "A":
            count += 1
            total += 11
        else:
            total += int(check)
    for _ in range(count):
        if total > 21:
            total -= 10
    print(total)

main()
