"""Coupon"""
def main():
    """calculate"""
    price = float(input())
    num_a, num_b = [float(i) for i in input().split()]
    num_x, num_y = [float(i) for i in input().split()]
    check1, check2 = price, price
    if price >= num_b:
        check1 = max(0, price - num_a)
    if price >= num_y:
        check2 = price * ((100-num_x)/100)
    if check1 == price and check2 == price:
        print("Nope")
    elif check1 == check2:
        if num_y < num_b:
            print(2, "%.1f" % check2)
        else:
            print(1, "%.1f" % check1)
    elif check1 < check2:
        print(1, "%.1f" % check1)
    elif check2 < check1:
        print(2, "%.1f" % check2)

main()
