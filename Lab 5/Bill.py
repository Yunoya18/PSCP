"""Bill"""
def main():
    """calculate"""
    price = int(input())
    service = price * 10/100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    total = (price + service) * 107/100
    print("%.2f" % total)

main()
