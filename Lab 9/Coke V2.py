"""Coke V2"""
def main():
    """calculate"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    if num_b == 0 or num_d < num_b:
        total = num_a * num_d
    else:
        total = (num_d * num_a) - ((num_a - num_c) * ((num_d  - 1)// num_b))
    print(total)

main()
