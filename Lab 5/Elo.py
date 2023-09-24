"""Elo"""
def main():
    """calculate"""
    r_a = int(input())
    r_b = int(input())
    team = input()
    elo_a = 1 / (1 + 10**((r_b - r_a)/400))
    elo_b = 1 / (1 + 10**((r_a - r_b)/400))
    if team == "A":
        print("%.2f" % elo_a)
    elif team == "B":
        print("%.2f" % elo_b)

main()
