"""Circular I"""
def main():
    """calculate"""
    num_xo = float(input())
    num_yo = float(input())
    radius = float(input())
    num_x = float(input())
    num_y = float(input())
    distance = ((num_xo - num_x)**2 + (num_yo - num_y)**2)**0.5
    if distance <= radius:
        print("Yes")
    else:
        print("No")

main()
