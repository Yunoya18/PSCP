"""Stamps"""
def main():
    """calculate"""
    times = int(input())
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    stamp = 0
    pay = 0
    for _ in range(times):
        cost = int(input())
        count = stamp // num_c
        for _ in range(count):
            cost -= num_d
            stamp -= num_c
            if cost <= 0:
                cost = 0
                break
        pay += cost
        get_stamp = (cost // num_a) * num_b
        stamp += get_stamp
    print(pay)
    print(stamp)

main()
