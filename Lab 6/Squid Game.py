"""Squid Game"""
def main():
    """calculate"""
    team_a = 0
    team_b = 0
    for _ in range(10):
        num = int(input())
        team_a += num
    for _ in range(10):
        num = int(input())
        team_b += num
    if team_a > team_b:
        print("B")
    elif team_a < team_b:
        print("A")
    else:
        print("AB")

main()
