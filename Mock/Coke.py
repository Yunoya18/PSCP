"""Coke"""
def main():
    """calculate"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    cost = 0
    if num_b != 0:
        for i in range(num_d):
            cost += num_a
            if i == (num_d-1):
                break
            else:
                if (i+1) % num_b == 0:
                    cost -= (num_a - num_c)
    else:
        cost = num_a * num_d
    print(cost)

main()
