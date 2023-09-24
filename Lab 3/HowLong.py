"""HowLong"""
def main():
    """process"""
    num = int(input())
    num = abs(num)
    num = str(num)
    total = 0
    for _ in num:
        total += 1
    print(total)

main()
