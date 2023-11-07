"""Tax"""
def main():
    """calculate"""
    year = int(input())
    engine = int(input())
    if year == 6:
        discount = 90/100
    elif year == 7:
        discount = 80/100
    elif year == 8:
        discount = 70/100
    elif year == 9:
        discount = 60/100
    elif year >= 10:
        discount = 50/100
    else:
        discount = 1
    total = ((min(600, engine) * 0.5) + (max(0, (min(1800, engine) - 600)) * 1.5) +\
             (max(0, engine - 1800) * 4)) * discount
    print("%.2f" % total)

main()
