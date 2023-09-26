"""Ticket Fare"""
def main():
    """calculate"""
    station = int(input())
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())
    num_f = int(input())
    num_g = int(input())
    num_station = abs(num_f - num_g)
    if num_f > station or num_g > station:
        total = "Error"
    elif num_station <= num_a - 1:
        total = num_b
    elif num_station <= num_a + num_c - 1:
        total = num_b + (num_d * (num_station - num_a))
    else:
        total = num_b + (num_d * num_c) + (num_e * (num_station - num_a - num_c))
    print(total)

main()
