"""CoinChangev1"""
def main():
    """process"""
    num = int(input())
    total_25 = num // 25
    num -= (25 * total_25)
    total_10 = num // 10
    num -= (10 * total_10)
    total_5 = num // 5
    num -= (5 * total_5)
    total_1 = num
    total = total_25 + total_10 + total_5 + total_1
    print(total)

main()
