"""WeightStation"""
def main():
    """calculate"""
    average = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    total = average * 4
    weight4 = total - weight1 - weight2 - weight3
    if total > 15000:
        print("Overweight")
    elif not average - (average / 2) <= weight1 <= average + (average / 2)\
        or not average - (average / 2) <= weight2 <= average + (average / 2)\
        or not average - (average / 2) <= weight3 <= average + (average / 2)\
        or not average - (average / 2) <= weight4 <= average + (average / 2):
        print("Unbalance")
    else:
        print("Pass %.2f" % weight4)

main()
