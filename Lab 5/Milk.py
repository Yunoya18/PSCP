"""Milk"""
def main():
    """calculate"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    get = num_d // num_a
    total = get
    if num_b == 0:
        print(total)
    else:
        while True:
            free = (get // num_b) * num_c
            left = get - ((get // num_b) * num_b)
            total += free
            left += free
            get = left
            if left < num_b:
                break
        print(total)

main()
