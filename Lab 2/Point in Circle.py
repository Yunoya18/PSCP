"""Point in Circle"""
def main():
    """calculate"""
    num_x = float(input())
    num_y = float(input())
    radius = float(input())
    num_xn = float(input())
    num_yn = float(input())
    distance = ((num_x - num_xn)**2 + (num_y - num_yn)**2)**0.5
    if distance > radius:
        print("False")
    else:
        print("True")

main()
