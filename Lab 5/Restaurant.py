"""Restaurant"""
def main():
    """calculate"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    price = num_a + num_d
    if num_a >= num_b:
        check = num_a * ((100-num_c)/100)
    else:
        check = num_a
    if price >= num_b:
        price = price * ((100-num_c)/100)
    if price > check:
        print("No %.3f" % (price - check))
    elif price < check:
        print("Yes %.3f" % (check - price))
    else:
        print("Yes")

main()
