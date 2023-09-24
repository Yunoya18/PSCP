"""Nearer"""
def main():
    """calculate"""
    alice = int(input())
    bob = int(input())
    car = int(input())
    dis_alice = abs(alice - car)
    dis_bob = abs(bob - car)
    if dis_alice > dis_bob:
        print("Bob", dis_bob)
    elif dis_alice == dis_bob:
        print("Sundaes", dis_alice)
    elif dis_alice < dis_bob:
        print("Alice", dis_alice)

main()
