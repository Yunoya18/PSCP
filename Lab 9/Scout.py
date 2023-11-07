"""Scout"""
def main():
    """calculate"""
    num_test = int(input())
    for _ in range(num_test):
        count = 0
        weight = 0
        _, can_get, max_weight = (int(i) for i in input().split())
        egg = sorted(list(map(int, input().split())))
        for egg_wieght in egg:
            weight += egg_wieght
            if weight <= max_weight:
                count += 1
        total = min(can_get, count)
        print(total)

main()
