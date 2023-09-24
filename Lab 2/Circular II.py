"""Circular II"""
def main():
    """calculate"""
    num_x = float(input())
    num_y = float(input())
    radius = float(input())
    other_x = float(input())
    other_y = float(input())
    other_radius = float(input())
    distance = ((num_x - other_x)**2 + (num_y - other_y)**2)**0.5
    if distance < radius + other_radius:
        print("Yes")
    else:
        print("No")

main()
