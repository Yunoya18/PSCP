"""Lift"""
def main():
    """calculate"""
    num = int(input())
    lift_weight = float(input())
    total_weight = 0
    under = 0
    higher = 0
    for _ in range(num):
        age = int(input())
        weight = float(input())
        if age < 12:
            under += 1
        else:
            higher += 1
        total_weight += weight
    if under != 0 and higher == 0:
        print("Not Safe")
    elif total_weight > lift_weight:
        print("Not Safe")
    else:
        print("Safe")

main()
