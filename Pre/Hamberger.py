"""Hamberger"""
def main():
    """calculate"""
    left = int(input())
    right = int(input())
    total = left * "|" + (left + right)*2 * "*" + right * "|"
    print(total)

main()
