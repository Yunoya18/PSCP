"""EuclideanDistance2D"""
def main():
    """calculate"""
    q_1 = float(input())
    q_2 = float(input())
    p_1 = float(input())
    p_2 = float(input())
    distance = ((q_1 - p_1)**2 + (q_2 - p_2)**2)**0.5
    print(distance)

main()
