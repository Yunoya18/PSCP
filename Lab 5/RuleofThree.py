"""RuleofThree"""
def main():
    """calculate"""
    check = 0
    final_price = 0
    final_weight = 0
    size = int(input())
    for _ in range(size):
        price = float(input())
        weight = float(input())
        if weight / price > check:
            check = weight / price
            final_price = price
            final_weight = weight
        elif weight / price == check:
            if price < final_price:
                final_price = price
                final_weight = weight
    print("%.2f %.2f" % (final_price, final_weight))

main()
