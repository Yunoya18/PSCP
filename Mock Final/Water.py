"""Water"""
def main():
    """calculate"""
    month = int(input())
    cost = float(input())
    check_extra = float(input())
    extra_cost = float(input())
    check = float(input())
    total = 0
    for _ in range(month):
        volume = float(input())
        price = (cost * min(volume, check_extra)) + (max(0, volume - check_extra) * extra_cost)
        if price > check:
            total += price
    print("%.2f" % total)

main()
